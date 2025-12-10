import allure

from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage

class TestProfilePage:
    @allure.title('Проверка клика по ссылке "Личный кабинет" авторизованного пользователя')
    def test_click_on_profile_button_authorized_user_profile_opened(self, driver, generate_user_data):
        email, password = generate_user_data
        page = ProfilePage(driver)
        page.login_user(email, password)
        page.click_on_profile_button()
        assert page.check_profile_page_is_loaded(), 'Страница профиля не загружена'

    @allure.title('Проверка клика по ссылке "Личный кабинет" авторизованного пользователя')
    def test_open_order_history_order_history_opened(self, driver, generate_user_data):
        email, password = generate_user_data
        profile_page = ProfilePage(driver)
        profile_page.login_user(email, password)
        constructor_page = ConstructorPage(driver)
        constructor_page.click_on_constructor_link()
        constructor_page.create_test_order()
        constructor_page.press_esc()
        profile_page.click_on_profile_button()
        profile_page.click_on_order_history_link()
        assert profile_page.check_order_history_is_loaded(), 'История заказов не загружена'

    @allure.title('Проверка клика по кнопке "Выход" авторизованного пользователя')
    def test_click_on_logout_button_form_opened(self, driver, generate_user_data):
        email, password = generate_user_data
        page = ProfilePage(driver)
        page.login_user(email, password)
        page.click_on_profile_button()
        page.click_on_logout_button()
        assert page.check_user_logged_out(), 'Пользователь не вышел из системы'