from seletools.actions import drag_and_drop
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators

from selenium.common.exceptions import TimeoutException



class MainPage(BasePage):
    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.wait_element_disappear(MainPageLocators.LOADING_SPINNER,5)
        self.wait_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на 'Лента заказов'")
    def click_order_feed(self):
        self.wait_element_disappear(MainPageLocators.LOADING_SPINNER,5)
        self.wait_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Выбрать первый ингредиент")
    def select_first_ingredient(self):
        self.wait_element_disappear(MainPageLocators.LOADING_SPINNER,5)
        self.wait_element_and_click(MainPageLocators.INGREDIENT_ITEM)

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
        self.wait_element_disappear(MainPageLocators.LOADING_SPINNER,100)
        order_number = self.find_element(MainPageLocators.ORDERS_IN_PROGRESS).text
        if(order_number == "9999"): #после обновления хром стал считывать это поля только со второго раза
            self.wait_element_disappear(MainPageLocators.LOADING_SPINNER,5)
            order_number = self.find_element(MainPageLocators.ORDERS_IN_PROGRESS).text
        self.wait_element_and_click(MainPageLocators.MODAL_CLOSE_BUTTON2)
        return order_number


    @allure.step("Проверить видимость деталей ингредиента")
    def is_ingredient_details_visible(self):
        try:
            return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)
        except TimeoutException:
            return False

    @allure.step("Закрыть модальное окно с деталями ингредиента")
    def close_ingredient_details(self):
        self.wait_element_and_click(MainPageLocators.MODAL_CLOSE_BUTTON)