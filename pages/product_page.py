import time

from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def click_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()


    def should_be_right_book(self):
        self.should_be_message()
        self.should_be_right_book_name()
        self.should_be_right_book_price()

    def should_disapear(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_MESSAGE), 'Message is not disapeared'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), 'There is no message'

    def should_be_right_book_name(self):
        assert self.get_element_text(*ProductPageLocators.BOOK_NAME)==self.get_element_text(*ProductPageLocators.BASKET_BOOK_NAME),\
            'Basket book name not equal book name'


    def should_be_right_book_price(self):
        assert self.get_element_text(*ProductPageLocators.BOOK_PRICE)==self.get_element_text(*ProductPageLocators.BASKET_BOOK_PRICE),\
            'Basket book name not equal book name'

