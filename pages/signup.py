from playwright.sync_api import Page

class Signup:
    def __init__(self,page:Page):
        self.page =                                           page
        self.mr_checkBox =                                    self.page.locator("#uniform-id_gender1")
        self.mrs_checkBox =                                   self.page.locator("#uniform-id_gender2")
        self.password =                                       self.page.locator("#password")
        self.newsletter_checkBox =                            self.page.locator("#newsletter")
        self.special_offer_checkBox =                         self.page.locator("#optin")
        self.signup_form =                                    self.page.locator(".login-form")
        self.firstname =                                      self.page.locator('[data-qa="first_name"]')
        self.lastname =                                       self.page.locator('[data-qa="last_name"]')
        self.company =                                        self.page.locator('[data-qa="company"]')
        self.address =                                        self.page.locator('[data-qa="address"]')
        self.country =                                        self.page.locator("#country")
        self.state =                                          self.page.locator("#state")
        self.zipcode =                                        self.page.locator("#zipcode")
        self.city =                                           self.page.locator("#city")
        self.mobile_number =                                  self.page.locator("#mobile_number")
        self.create_account =                                 self.page.locator('[data-qa="create-account"]')
        self.day =                                            self.page.locator("#days")
        self.month =                                          self.page.locator("#months")
        self.year =                                           self.page.locator("#years")
        self.account_created =                                self.page.locator('[data-qa="account-created"]')


    def signup_form_check(self):
        return self.signup_form

    def signup(self,status,firstname,lastname,password,day,month,year,company,address,country,state,zipcode,city,mobile_number):

        self.password.fill(password)
        if status == "married":
            self.mr_checkBox.click()
        else:
            self.mrs_checkBox.click()

        self.day.select_option(day)
        self.month.select_option(month)
        self.year.select_option(year)

        self.newsletter_checkBox.click()
        self.special_offer_checkBox.click()
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)

        self.company.fill(company)
        self.address.fill(address)
        self.country.select_option(country)
        self.state.fill(state)
        self.zipcode.fill(zipcode)
        self.city.fill(city)
        self.mobile_number.fill(mobile_number)
        self.create_account.click(timeout = 5000)

    def signup_done(self):
        return self.account_created