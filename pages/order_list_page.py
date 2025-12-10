import random

import allure

from data import Urls
from locators.athorization_locators import AuthFormsLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageButtonLocators
from locators.order_list_page_locators import OrderListPageLocators


class OrderListPage(BasePage):
    @allure.step('Переход на страницу "Лента заказов"')
    def go_to_order_list_page(self):
        self.go_to_url(f'{Urls.BASE_URL}{Urls.ORDER_LIST_URL}')

    @allure.step('Нажатие на ссылку "Лента заказов"')
    def click_on_order_list_link(self):
        self.wait_for_element_to_disappear(AuthFormsLocators.INVISIBLE_OVERLAY)
        self.wait_and_click_element(MainPageButtonLocators.ORDER_LIST_LINK)

    @allure.step('Выбор и возврат произвольного заказа из списка')
    def get_random_order_from_list(self):
        orders_list = self.wait_and_get_elements(OrderListPageLocators.ORDERS_LIST_IN_FEED)
        order = orders_list[random.randint(0, len(orders_list)-1)]
        return order

    @allure.step('Получение номеров заказов из ленты заказов')
    def get_feed_orders_numbers_list(self):
        feed_orders = self.wait_and_get_elements(OrderListPageLocators.ORDERS_LIST_IN_FEED)
        feed_orders_numbers_list = [order.text for order in feed_orders]
        return feed_orders_numbers_list

    @allure.step('Проверка, что заказы из профиля есть в ленте заказов')
    def missing_profile_orders_in_feed(self, profile_orders, feed_orders):
        missing_orders = [order.text for order in profile_orders if order not in feed_orders]
        return missing_orders

    @allure.step('Получение значения счетчика выполненных сегодня заказов')
    def get_todays_successful_orders(self):
        todays_successful_orders_counter = self.wait_and_get_element(OrderListPageLocators.TODAYS_SUCCESSFUL_ORDERS_COUNT).text
        return todays_successful_orders_counter

    @allure.step('Получение значения счетчика всех выполненных заказов')
    def get_total_successful_orders(self):
        total_successful_orders_counter = self.wait_and_get_element(OrderListPageLocators.TOTAL_SUCCESSFUL_ORDERS_COUNT).text
        return total_successful_orders_counter

    @allure.step('Получение списка заказов в работе')
    def get_orders_in_work_list(self):
        orders = self.wait_and_get_elements(OrderListPageLocators.ORDERS_IN_WORK_LIST)
        orders_in_work_list = [order.text for order in orders]
        return orders_in_work_list

    @allure.step('Ожидание обновления списка "В работе"')
    def wait_for_in_work_list_refresh(self):
        self.wait.until_not(lambda x: 'Все текущие заказы готовы!' in
                                      self.wait_and_get_elements(OrderListPageLocators.ORDERS_IN_WORK_LIST)[0].text)

    @allure.step('Проверка, что открылись детали заказа')
    def check_order_details_opened(self):
        order_details = self.wait_and_get_element(OrderListPageLocators.ORDER_DETAILS_MODAL)
        return order_details.is_displayed()

    @allure.step('Проверка загрузки страницы "Лента заказов"')
    def check_order_list_page_loaded(self):
        order_list = self.wait_and_get_element(OrderListPageLocators.ORDER_FEED)
        return order_list.is_displayed()
