import allure

from pages.order_page import OrderPage

@allure.feature("Главная страница")
class TestOrderPage:

    @allure.title("Увеличение счетчиков заказов за все время")
    def test_go_to_order_total(self, driver):
        order_feed_page = OrderPage(driver)
        order_feed_page.go_to_login()
        order_feed_page.login()
        order_feed_page.click_order_feed()
        initial_total = order_feed_page.get_total_orders()

        order_feed_page.click_constructor()

        order_feed_page.add_ingredient_to_order()
        order_feed_page.create_order()

        order_feed_page.click_order_feed()
        new_initial_total = order_feed_page.get_total_orders()

        assert int(initial_total) < int(new_initial_total), \
            f"Счетчик не увеличился: было {initial_total}, стало {new_initial_total}"


    @allure.title("Увеличение счетчиков заказов за сегодня")
    def test_go_to_order_today(self, driver):
        order_feed_page = OrderPage(driver)
        order_feed_page.go_to_login()
        order_feed_page.login()
        order_feed_page.click_order_feed()
        initial_today = order_feed_page.get_today_orders()

        order_feed_page.click_constructor()

        order_feed_page.add_ingredient_to_order()
        order_feed_page.create_order()

        order_feed_page.click_order_feed()
        new_initial_today = order_feed_page.get_today_orders()

        assert int(initial_today) < int(new_initial_today), \
            f"Счетчик не увеличился: было {initial_today}, стало {new_initial_today}"



    @allure.title("Заказ в работе")
    def test_is_order_in_progress(self, driver):
        order_feed_page = OrderPage(driver)
        order_feed_page.go_to_login()
        order_feed_page.login()
        order_feed_page.click_constructor()
        order_feed_page.add_ingredient_to_order()
        initial_number = order_feed_page.create_order()
        order_feed_page.click_order_feed()
        new_initial_number = order_feed_page.get_current_orders()
        assert int(initial_number) == int(new_initial_number)


