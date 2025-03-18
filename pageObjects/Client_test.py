from playwright.sync_api import Page


class ClientTest:

    def __init__(self, page: Page):
        self.page = page

    @property
    def client_code_input(self):
        return self.page.locator("input[name='clientCode']")

    def fill_client_code(self, client_code: str):
        self.client_code_input.fill(client_code)

    @property
    def environment_select(self):
        return self.page.locator("select[name='environment']")

    def select_environment(self, environment: str):
        self.environment_select.select_option(environment)

    @property
    def show_detail_button(self):
        return self.page.locator('input[type="submit"][value="Show Detail"]')

    def click_show_detail(self):
        self.show_detail_button.click()

    @property
    def first_name_input(self):
        return self.page.locator('input[name="fn"]')

    def fill_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    @property
    def last_name_input(self):
        return self.page.locator('input[name="ln"]')

    def fill_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    @property
    def amount_input(self):
        return self.page.locator('input[name="amt"]')

    def fill_amount(self, amount: str):
        self.amount_input.fill(amount)

    @property
    def contact_input(self):
        return self.page.locator('input[name="con"]')

    def fill_contact(self, contact: str):
        self.contact_input.fill(contact)

    @property
    def email_input(self):
        return self.page.locator('input[name="email"]')

    def fill_email(self, email: str):
        self.email_input.fill(email)

    @property
    def pay_button(self):
        return self.page.locator("input[type='submit'][value='Pay']")

    def click_pay(self):
        self.pay_button.click()

    @property
    def error_message(self):
        return self.page.locator("h1")

    def get_error_message_text(self):
        return self.error_message.text_content()

    @property
    def mer_client_code_input(self):
        return self.page.locator("input[name='clientCode']")

    def enter_client_code(self, code: str):
        self.mer_client_code_input.fill(code)

    @property
    def name_message(self):
        return self.page.locator("h3[id='clientName']")

    def get_name_text(self):
        return self.name_message.text_content()

