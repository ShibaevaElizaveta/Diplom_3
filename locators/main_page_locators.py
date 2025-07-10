from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and text()='Лента Заказов']")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient__')][1]")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p.text_type_digits-medium.mr-3")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__container')]")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__') and .//h2[text()='Детали ингредиента']]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close__')]")
    MODAL_LOCATOR = (By.CSS_SELECTOR, "img[alt='tick animation']")
    LOADING_SPINNER = (By.CSS_SELECTOR, "img[src*='loading'][alt='loading animation']")
    MODAL_CLOSE_BUTTON2 = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified') and contains(@class, 'Modal_modal__close')]")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, "h2.text.text_type_digits-large.mb-8")