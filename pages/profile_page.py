import allure

from pages.base_page import BasePage
from data import Urls
from locators.athorization_locators import AuthButtonLocators, AuthFormsLocators
from locators.profile_page_locators import ProfilePageElementsLocators
from locators.main_page_locators import MainPageButtonLocators

class ProfilePage(BasePage):
    @allure.step('Авторизация пользователя')
    def login_user(self, email, password):
        self.go_to_url(f'{Urls.BASE_URL}{Urls.FRONT_LOGIN_USER_URL}')
        self.set_field(AuthFormsLocators.LOGIN_EMAIL_INPUT, email)
        self.set_field(AuthFormsLocators.LOGIN_PASSWORD_INPUT, password)
        self.wait_for_element_to_disappear(AuthFormsLocators.INVISIBLE_OVERLAY)
        self.wait_and_click_element(AuthButtonLocators.SUBMIT_BUTTON)

    @allure.step('Переход по кнопке "Профиль"')
    def click_on_profile_button(self):
        self.wait_for_element_to_disappear(AuthFormsLocators.INVISIBLE_OVERLAY)
        self.wait_and_click_element(MainPageButtonLocators.GO_TO_PROFILE_BUTTON)

    @allure.step('Переход по кнопке "История заказов"')
    def click_on_order_history_link(self):
        self.wait_for_element_to_disappear(AuthFormsLocators.INVISIBLE_OVERLAY)
        self.wait_and_click_element(ProfilePageElementsLocators.ORDER_HISTORY_LINK)

    @allure.step('Переход по кнопке "Выход"')
    def click_on_logout_button(self):
        self.wait_for_element_to_disappear(AuthFormsLocators.INVISIBLE_OVERLAY)
        self.wait_and_click_element(ProfilePageElementsLocators.LOGOUT_BUTTON)

    @allure.step('Получение номеров заказов из профиля')
    def get_profile_orders_numbers_list(self):
        orders = self.wait_and_get_elements(ProfilePageElementsLocators.ORDERS_LIST_IN_PROFILE)
        orders_numbers_list = []
        for order in orders:
            orders_numbers_list.append(order.text)
        return orders_numbers_list

    @allure.step('Проверка загрузки истории заказов')
    def check_order_history_is_loaded(self):
        order_history_list = self.wait_and_get_element(ProfilePageElementsLocators.ORDER_HISTORY_LIST)
        return order_history_list.is_displayed()

    @allure.step('Проверка загрузки страницы профиля')
    def check_profile_page_is_loaded(self):
        profile_link = self.wait_and_get_element(ProfilePageElementsLocators.PROFILE_LINK)
        return profile_link.is_displayed()

    @allure.step('Проверка выхода из профиля')
    def check_user_logged_out(self):
        email_input = self.wait_and_get_element(AuthFormsLocators.LOGIN_EMAIL_INPUT)
        return email_input.is_displayed()

