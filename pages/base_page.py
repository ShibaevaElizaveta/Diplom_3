from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator, timeout=10):
        try:
            element = self.find_element(locator, timeout)

            return element.is_displayed()
        except:
            return False