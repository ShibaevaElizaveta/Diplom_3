from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from urls import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Urls.main

    @allure.step("Ожидаем закрытие модального окна")
    def wait_element_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ожидаем объект и нажимаем на него")
    def wait_element_and_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Видимость элемента")
    def is_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()


    @allure.step("Возвращает текущую страницу")
    def get_cur_url(self):
        return self.driver.current_url

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Открыть страницу")
    def fill_element(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

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