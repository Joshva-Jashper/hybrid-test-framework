from playwright.sync_api import Page

class ContactUs:
    def __init__(self,page:Page):
        self.page =            page
        self.Contact_header =          self.page.get_by_text("Get In Touch")
        self.Contact_Name =            self.page.get_by_placeholder("Name",exact=True)
        self.Contact_Email =           self.page.get_by_placeholder("Email",exact=True)
        self.Contact_Subject =         self.page.get_by_placeholder("Subject",exact=True)
        self.Contact_comment =         self.page.get_by_placeholder("Your Message Here",exact=True)
        self.Contact_file =            self.page.locator('[name="upload_file"]')
        self.submit_button =           page.get_by_role("button", name="Submit")
        self.conformation_msg =        self.page.get_by_text("Success! Your details have been submitted successfully.",exact = True)





    def get_contact_header(self):
        return self.Contact_header

    def fill_contact_details(self,name,email,subject,comment,file_path):
        self.Contact_Name.fill(name)
        self.Contact_Email.fill(email)
        self.Contact_Subject.fill(subject)
        self.Contact_comment.fill(comment)
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_button.dblclick(force=True)   
        self.page.wait_for_load_state("networkidle")

    def get_conformation_msg(self):
        return self.conformation_msg    


        
