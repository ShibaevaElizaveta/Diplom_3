from selenium.webdriver import ActionChains
import time
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators
from locators.order_page_locators import LoginPageLocators
import allure
from data import UserData


class OrderPage(MainPage):
    @allure.step("Получить общее количество заказов")
    def login(self):

        self.driver.find_element(*LoginPageLocators.login_input).send_keys(UserData.email)
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(UserData.password)
        time.sleep(1)
        self.driver.find_element(*LoginPageLocators.login_button).click()
        time.sleep(1)
        return

    @allure.step("Зайти на страницу логина")
    def go_to_login(self):
        self.driver.get(f"https://stellarburgers.nomoreparties.site/login")

    @allure.step("Кликнуть на 'Лента заказов'")
    def click_order_feed(self):
        time.sleep(1)
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
