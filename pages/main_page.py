from seletools.actions import drag_and_drop
import time
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        time.sleep(2)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на 'Лента заказов'")
    def click_order_feed(self):
        time.sleep(2)
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Выбрать первый ингредиент")
    def select_first_ingredient(self):
        time.sleep(2)
        self.click_element(MainPageLocators.INGREDIENT_ITEM)

    @allure.step("Проверить отображение деталей ингредиента")
    def is_ingredient_details_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
            return True
        except:
            return False

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self):
        drop_area = self.find_element(MainPageLocators.DROP_AREA)
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        drag_and_drop(self.driver, ingredient, drop_area)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        return self.find_element(MainPageLocators.INGREDIENT_COUNTER).text

    @allure.step("Создать заказ")
    def create_order(self):
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)
        time.sleep(5)
        order_number = self.find_element(MainPageLocators.ORDERS_IN_PROGRESS).text
        time.sleep(2)
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON2)
        return order_number


    @allure.step("Проверить видимость деталей ингредиента")
    def is_ingredient_details_visible(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_MODAL)
            ).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Закрыть модальное окно с деталями ингредиента")
    def close_ingredient_details(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        ).click()