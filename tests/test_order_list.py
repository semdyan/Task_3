import allure

from pages.order_list_page import OrderListPage
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage

class TestOrderListPage:
    @allure.title('Проверка клика по ссылке "Конструктор"')
    def test_click_on_constructor_link_constructor_page_opened(self, driver):
        order_list_page = OrderListPage(driver)
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        order_list_page.click_on_order_list_link()
        assert order_list_page.check_order_list_page_loaded(), 'Страница "Лента заказов" не открылась'

    @allure.title('Проверка отображения деталей заказа')
    def test_check_order_details_displayed(self, driver, generate_user_data):
        page = OrderListPage(driver)
        page.go_to_order_list_page()
        order = page.get_random_order_from_list()
        order.click()
        assert page.check_order_details_opened(), 'Детали заказа не отображаются'

    @allure.title('Проверка, что заказы пользователя отображаются в списке')
    def test_check_user_orders_displayed_in_order_list(self, driver, generate_user_data):
        email, password = generate_user_data
        profile_page = ProfilePage(driver)
        profile_page.login_user(email, password)
        constructor_page = ConstructorPage(driver)
        constructor_page.create_test_order()
        constructor_page.press_esc()
        profile_page.click_on_profile_button()
        profile_page.click_on_order_history_link()
        profile_orders = profile_page.get_profile_orders_numbers_list()
        order_list_page = OrderListPage(driver)
        order_list_page.go_to_order_list_page()
        feed_orders = order_list_page.get_feed_orders_numbers_list()
        missing_orders = order_list_page.missing_profile_orders_in_feed(profile_orders, feed_orders)
        assert not missing_orders, f'В ленте заказов отсутствуют заказы: {missing_orders}'

    @allure.title('Проверка, что счетчик выполненных заказов за сегодня обновляется при создании нового заказа')
    def test_todays_successful_orders_counter_updates_on_new_order(self, driver, generate_user_data):
        email, password = generate_user_data
        order_list_page = OrderListPage(driver)
        order_list_page.go_to_order_list_page()
        initial_count = order_list_page.get_todays_successful_orders()
        profile_page = ProfilePage(driver)
        profile_page.login_user(email, password)
        constructor_page = ConstructorPage(driver)
        constructor_page.create_test_order()
        order_list_page.go_to_order_list_page()
        order_list_page.wait_for_in_work_list_refresh()
        updated_count = order_list_page.get_todays_successful_orders()
        assert updated_count > initial_count, 'Счетчик выполненных заказов за сегодня не обновляется'

    @allure.title('Проверка, что счетчик выполненных заказов за все время обновляется при создании нового заказа')
    def test_total_successful_orders_counter_updates_on_new_order(self, driver, generate_user_data):
        email, password = generate_user_data
        order_list_page = OrderListPage(driver)
        order_list_page.go_to_order_list_page()
        initial_count = order_list_page.get_total_successful_orders()
        profile_page = ProfilePage(driver)
        profile_page.login_user(email, password)
        constructor_page = ConstructorPage(driver)
        constructor_page.create_test_order()
        order_list_page.go_to_order_list_page()
        order_list_page.wait_for_in_work_list_refresh()
        updated_count = order_list_page.get_total_successful_orders()
        assert updated_count > initial_count, 'Счетчик выполненных заказов за все время не обновляется'

    @allure.title('Проверка, что номер заказа появляется в списке "В работе"')
    def test_order_number_in_making_list(self, driver, generate_user_data):
        email, password = generate_user_data
        profile_page = ProfilePage(driver)
        profile_page.login_user(email, password)
        constructor_page = ConstructorPage(driver)
        order = '0' + constructor_page.create_test_order()
        order_list_page = OrderListPage(driver)
        order_list_page.go_to_order_list_page()
        order_list_page.wait_for_in_work_list_refresh()
        orders_in_work = order_list_page.get_orders_in_work_list()
        assert order in orders_in_work, 'Номер заказа не появляется в списке "В работе"'
