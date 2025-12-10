import allure

from pages.order_list_page import OrderListPage
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage

class TestConstructorPage:
    @allure.title('Проверка клика по ссылке "Конструктор"')
    def test_click_on_constructor_link_constructor_page_loaded(self, driver):
        order_list_page = OrderListPage(driver)
        constructor_page = ConstructorPage(driver)
        order_list_page.go_to_order_list_page()
        constructor_page.click_on_constructor_link()
        assert constructor_page.check_constructor_page_loaded(), 'Страница конструктора не загрузилась'

    @allure.title('Проверка клика по случайному ингредиенту')
    def test_click_on_random_ingredient_details_loaded(self, driver):
        page = ConstructorPage(driver)
        page.open_constructor_page()
        ingredient =page.return_random_ingredient()
        page.scroll_to_element_by_element(ingredient)
        ingredient.click()
        assert page.check_ingredient_details_opened(), 'Детали ингредиента не открылись'

    @allure.title('Проверка клика по кнопке закрытия деталей ингредиента')
    def test_click_on_close_ingredient_details_button_details_closed(self, driver):
        page = ConstructorPage(driver)
        page.open_constructor_page()
        ingredient = page.return_random_ingredient()
        page.scroll_to_element_by_element(ingredient)
        ingredient.click()
        page.click_on_close_ingredient_details_button()
        assert page.check_ingredient_details_closed(), 'Детали ингредиента не закрылись'

    @allure.title('Проверка изменения каунтера при добавлении ингредиента в заказ')
    def test_add_ingredient_to_order_counter_changed(self, driver):
        page = ConstructorPage(driver)
        page.open_constructor_page()
        counter_initial_value = page.get_basket_counter_value()
        ingredient = page.return_random_ingredient()
        page.scroll_to_element_by_element(ingredient)
        page.drag_and_drop_to_basket(ingredient)
        counter_final_value = page.get_basket_counter_value()
        assert counter_final_value > counter_initial_value, 'Счетчик цены не изменился'

    @allure.title('Проверка успешного заказа авторизованным пользователем')
    def test_confirm_order_authorized_user_order_placed(self, driver, generate_user_data):
       email, password = generate_user_data
       constructor_page = ConstructorPage(driver)
       profile_page = ProfilePage(driver)
       profile_page.login_user(email, password)
       constructor_page.add_test_burger_to_basket()
       constructor_page.click_on_confirm_order_button()
       assert constructor_page.return_order_number(), 'Заказ не оформлен'

