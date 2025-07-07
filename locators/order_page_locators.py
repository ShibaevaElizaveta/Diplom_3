from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDERS_TOTAL = (By.CLASS_NAME, "OrderFeed_number__2MbrQ")
    ORDERS_TODAY = (By.CLASS_NAME, "OrderFeed_number__2MbrQ")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, "h2.text.text_type_digits-large.mb-8")
    CURRENT_ORDER_NUMBER_ITEM = (By.CSS_SELECTOR, "li.text.text_type_digits-default.mb-2")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and text()='Лента Заказов']")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")

    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified') and contains(@class, 'Modal_modal__close')]")

    CLOSE_ICON = (By.XPATH, "//svg[@width='24' and @height='24' and @viewBox='0 0 24 24' and @fill='#F2F2F3']")

class LoginPageLocators:
    login_label = (By.XPATH, "//h2[text()='Вход']")                          # Заголовок "Вход"
    login_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
    login_button = (By.XPATH, "//button[text()='Войти']")                     # Кнопка "Войти"
    registration_link = (By.XPATH, "//a[@href='/register']")                  # Ссылка "Зарегистрироваться"
    account_link = (By.XPATH, "//a[@href='/account']")
    restore_password_link = (By.XPATH, "//a[@href='/forgot-password']")       # Ссылка "Восстановить пароль"

