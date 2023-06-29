from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketLocators.EMPTY_MESSAGE)

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.ITEMS_IN_BASKET)
