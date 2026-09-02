from playwright.sync_api import Playwright, expect
import pytest
from pathlib import Path
import allure
from pages.ui.base_page import BasePage
from pages.ui.signup import Signup
from pages.ui.login_signup_page import LoginSignupPage

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


@pytest.fixture(scope = "session")
def get_storage_state(request,playwright:Playwright):
    browser = playwright.chromium.launch()
    browser_context = browser.new_context()
    page = browser_context.new_page()
    base_url = get_option(request.config,"base_url")
    page.goto(base_url,wait_until="domcontentloaded",timeout=60000)

    base_page = BasePage(page)
    login_page = LoginSignupPage(page)
    base_page.click_signup_login()
    login_page.login("john.smith.q02@example.com", "AnotherPass@456")
    expect(login_page.success_full_login()).to_be_visible()

    token_path = "auth/token.json"
    browser_context.storage_state(path = token_path)
    yield token_path
    browser_context.close()
    browser.close()




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"report_{report.when}", report)

@pytest.fixture(scope = "function")
def browser_context(request,playwright:Playwright,get_storage_state):
    browser_name = get_option(request.config,"browser")
    video_option = get_option(request.config,"video")
    headed_flag = get_option(request.config,"headed")
    print("[*] Playwright is started....")
    print(f"[*] Playwright browser is started....{browser_name}")
    print(f"[*] starting with video mode ...{video_option}")
    #print(f"[*] headed flagg is set to {headed_flag}")
    if browser_name == "chromium":
        browser = playwright.chromium.launch()
    elif browser_name == "firefox":
        browser = playwright.firefox.launch()
    elif browser_name == "webkit":
        browser = playwright.webkit.launch()
    else:
        raise Exception("[*] Browser type not supported")

    if "no_auth" in request.node.keywords:
        context = browser.new_context()
    else:
        if video_option in ["on","retain-on-failure"]:
            print("[*] video started based on requirements.....")
            context = browser.new_context(record_video_dir = "report/videos",storage_state = get_storage_state)
        else:
            print("[*] video not started based on requirements......")
            context = browser.new_context(storage_state=get_storage_state)

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
    page.goto(base_url,wait_until="domcontentloaded",timeout=60000)
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





















