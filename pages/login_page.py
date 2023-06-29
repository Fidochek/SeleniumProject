from .base_page import BasePage
from .locators import LoginPageLocators
import time


        # self.email = f'{str(time.time())}@fakemail.org'
        # self.password = secrets.token_urlsafe(8)
class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.input_registration_email(email)
        self.input_registration_password(password)
        self.click_registration_button()

    def input_registration_email(self, email: str):
        input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        input.send_keys(email)

    def input_registration_password(self, password: str):
        input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_INPUT)
        input1.send_keys(password)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_INPUT)
        input2.send_keys(password)

    def click_registration_button(self):
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, 'Wrong URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form is not presented'