from playwright.sync_api import Playwright, sync_playwright
import pytest
from pathlib import Path
import allure

#
# def pytest_addoption(parser):
#     parser.addoption("--browser",action = "store",default = "chromium")
#     parser.addoption("--video",action = "store", default = "off")
#     parser.addoption("--headed",action = "store",default = "True")
#     parser.addoption("--screenshot",action = "store", default = "only_on_failure")
#     parser.addoption("--tracing",action = "store", default = "retain_on_failure")
#     parser.addoption("--base-url",action = "store", default = "https://automationexercise.com/")
#


def get_option(config,cmd_option):
    cmd = config.getoption(cmd_option)
    if cmd is not None:
        return str(cmd[0]) if isinstance(cmd,list) else str(cmd)
    elif cmd_option == "headed":
        value = config.getini(cmd_option).lower()
        return True if value == "true" else False
    else:
        return config.getini(cmd_option)





@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"report_{report.when}", report)

@pytest.fixture(scope = "function")
def browser_context(request,playwright:Playwright):
    browser_name = get_option(request.config,"browser")
    video_option = get_option(request.config,"video")
    #headed_flag = get_option(request.config,"headed")


    print("[*] Playwright is started....")
    print(f"[*] Playwright browser is started....{browser_name}")
    print(f"[*] starting with video mode ...{video_option}")
    #print(f"[*] headed flagg is set to {headed_flag}")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless= True)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless= True)
    else:
        raise Exception("[*] Browser type not supported")

    if video_option in ["on","retain-on-failure"]:
        print("[*] video started based on requirements.....")
        context = browser.new_context(record_video_dir = "report/videos")
    else:
        print("[*] video not started based on requirements......")
        context = browser.new_context()

    yield context

    print("[*] context closed")
    print("[*] browser closed")
    print("[*] playwright stopped")

    context.close()
    browser.close()


@pytest.fixture(scope="function")
def page(browser_context,request):
    base_url = get_option(request.config,"base_url")
    screenshot_option = get_option(request.config,"screenshot")
    tracing_option = get_option(request.config,"tracing")
    video_option = get_option(request.config,"video")

    if tracing_option in ["on", "retain-on-failure"]:
        print(f"[*] tracing started on requirements....{tracing_option}")
        browser_context.tracing.start(screenshots = True,snapshots = True)

    page = browser_context.new_page()
    page.goto(base_url)
    yield page

    test_name = request.node.name
    test_failed_or_passed = hasattr(request.node,"report_call") and request.node.report_call.failed

    if tracing_option in ["on","retain-on-failure"]:
        path = f"report/traicng/{test_name}.zip"
        print(f"[*] tracing files is stored in ===> {path}")
        browser_context.tracing.stop(path=path)

    if test_failed_or_passed and screenshot_option in ["on","only-on-failure"]:
        path = f"report/screenshot/{test_name}.png"
        page.screenshot(path=path)
        print(f"[*] screenshot is stored ===> {path}")

        allure.attach.file(
            path,
            name = f"{test_name}_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    if test_failed_or_passed and video_option in ["on","retain_on_failure"]:
        video_path = page.video.path() if page.video else None
        if video_path and Path(video_path).exists():
            allure.attach.file(
                video_path,
                name = f"{test_name}_video",
                attachment_type=allure.attachment_type.MP4,
            )


















