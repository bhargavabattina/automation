from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def email_input(self):
        return self.page.get_by_role("textbox", name="Email Address")



    def fill_email(self, email: str):
        self.email_input.fill(email)

    @property
    def password_input(self):
        return self.page.get_by_role("textbox", name="Password")

    def fill_password(self, password: str):
        self.password_input.fill(password)

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Sign In")

    def click_login(self):
        self.login_button.click()


    @property
    def valid_message(self):
        return self.page.get_by_role("heading", name="Dashboard")

    def get_valid_message_text(self):
        return self.valid_message.text_content()


    @property
    def name_message(self):
        return self.page.locator("h3[id='clientName']")

    def get_name_text(self):
        return self.name_message.text_content()



