import pytest

from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com'
        self.browser = browser
        self.page = BasePage(self.browser, self.link)
        self.page.open()
        yield
    def test_guest_can_go_to_login_page(self):
        login_page = self.page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self):
        basket_page = self.page.go_to_basket_page()
        basket_page = BasketPage(self.browser, self.browser.current_url)
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_empty_basket()