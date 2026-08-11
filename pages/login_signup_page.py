from playwright.sync_api import Page


class LoginSignupPage:
    def __init__(self,page):
        self.page =                         page
        self.login_form =                   self.page.locator(".login-form")
        self.login_email =                  self.page.locator('[data-qa="login-email"]')
        self.login_password =               self.page.get_by_placeholder("Password")
        self.login_button =                 self.page.locator('[data-qa="login-button"]')
        self.signup_form =                  self.page.locator(".signup-form")
        self.signup_name =                  self.page.get_by_placeholder("Name")
        self.signup_email =                 self.page.locator('[data-qa="signup-email"]')
        self.signup_button =                self.page.locator('[data-qa="signup-button"]')
        self.user_exists =                  self.page.locator('p:has-text("Email Address already exist!")')
        self.logged_in =                    self.page.locator('[class="fa fa-user"]')
        self.login_error =                  self.page.locator('p:has-text("Your email or password is incorrect!")')
        self.logout_button =                self.page.locator('[href="/logout"]')
        self.delete_account =               self.page.locator('[href="/delete_account"]')
        self.account_deleted =              self.page.locator('[class="title text-center"] b')


    def signup(self,email,username):
        self.signup_name.fill(username)
        self.signup_email.fill(email)
        self.signup_button.click(timeout = 5000)

    def check_signup_form(self):
        return self.signup_form

    def check_login_form(self):
        return self.login_form

    def login(self,email,password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click(timeout = 5000)

    def check_user_exists(self):
        return self.user_exists

    def success_full_login(self):
        return self.logged_in

    def not_success_full_login(self):
        return self.login_error

    def click_logout_button(self):
        self.logout_button.click(timeout = 3000)

    def click_delete_account(self):
        self.delete_account.click(timeout = 3000)

    def account_deleted_msg(self):
        return self.account_deleted

