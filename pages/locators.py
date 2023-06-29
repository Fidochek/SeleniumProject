from selenium.webdriver.common.by import By


class BasketLocators():
    EMPTY_MESSAGE = (By.ID, 'content_inner')
    EMPTY_MESSAGE_INVALID = (By.ID, 'content_inner_invalid')

    ITEMS_IN_BASKET = (By.ID, 'basket-items')
    ITEMS_IN_BASKET_INVALID = (By.ID, 'basket-items_invalid')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a')

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_URL = 'login'

    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')

    REGISTRATION_EMAIL_INPUT = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD1_INPUT = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD2_INPUT = (By.NAME, 'registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-primary')
    BOOK_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main p.price_color')

    BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon:nth-child(1) .alertinner')
    BASKET_BOOK_NAME = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon:nth-child(1) .alertinner strong')
    BASKET_BOOK_PRICE = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon:nth-child(3) .alertinner p strong')