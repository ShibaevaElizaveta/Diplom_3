from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators
from locators.order_page_locators import LoginPageLocators
import allure

from urls import Urls


class OrderPage(MainPage):
    @allure.step("Получить общее количество заказов")
    def login(self,email,pwd):
        self.fill_element(LoginPageLocators.login_input,email)
        self.fill_element(LoginPageLocators.password_input,pwd)
        self.wait_element_disappear(OrderPageLocators.LOADING_SPINNER,5)
        self.wait_element_and_click(LoginPageLocators.login_button)
        self.wait_element_disappear(OrderPageLocators.LOADING_SPINNER,5)
        return

    @allure.step("Зайти на страницу логина")
    def go_to_login(self):
        self.open(Urls.login)

    @allure.step("Кликнуть на 'Лента заказов'")
    def click_order_feed(self):
        self.wait_element_disappear(OrderPageLocators.LOADING_SPINNER,5)
        self.click_element(OrderPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Получить общее количество заказов")
    def get_total_orders(self):
        return self.find_element(OrderPageLocators.ORDERS_TOTAL).text

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        return self.find_element(OrderPageLocators.ORDERS_TODAY).text

    @allure.step("Получить количество заказов за сегодня")
    def get_current_orders(self):
        return self.find_element(OrderPageLocators.CURRENT_ORDER_NUMBER_ITEM).text
