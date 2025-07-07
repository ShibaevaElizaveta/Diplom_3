import allure

from pages.main_page import MainPage

@allure.feature("Главная страница")
class TestMainPage:
    @allure.title("Переход в конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()


    @allure.title("Переход в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()


    @allure.title("Отображение деталей ингредиента")
    def test_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.select_first_ingredient()
        assert main_page.is_ingredient_details_visible()

    @allure.title("Закрытие модального окна")
    def test_close_modal(self, driver):
        main_page = MainPage(driver)
        main_page.select_first_ingredient()
        was_closed = main_page.close_modal()
        assert was_closed or not main_page.is_ingredient_details_visible()

    @allure.title("Увеличение счетчика ингредиента")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        initial_count = main_page.get_ingredient_counter() or "0"

        main_page.add_ingredient_to_order()
        new_count = main_page.get_ingredient_counter()
        assert int(new_count) > int(initial_count)
        #assert 1 > int(initial_count)

