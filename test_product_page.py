import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time, secrets

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        registration_email = f'{str(time.time())}@fakemail.org'
        registration_password = secrets.token_urlsafe(8)
        self.link = link
        self.browser = browser
        self.page = ProductPage(self.browser, self.link)
        self.page.open()
        self.login_page = self.page.go_to_login_page()
        self.login_page = LoginPage(self.browser, self.link)
        self.login_page.register_new_user(registration_email, registration_password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.page.click_basket_button()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    browser = browser
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_right_book()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
    browser = browser
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser = browser
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    page.solve_quiz_and_get_code()
    page.should_disapear()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    browser = browser
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    browser = browser
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    browser = browser
    page = ProductPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket()
