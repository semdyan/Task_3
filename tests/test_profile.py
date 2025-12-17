import allure

from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage

class TestProfilePage:
    @allure.title('Проверка клика по ссылке "Личный кабинет" авторизованного пользователя')
    def test_click_on_profile_button_authorized_user_profile_opened(self, driver, generate_user_data):
        email, password = generate_user_data
        profile_page = ProfilePage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page.set_credentials(email, password)
        constructor_page.wait_for_overlay_to_disappear()
        profile_page.click_on_submit_button()
        constructor_page.wait_for_overlay_to_disappear()
        profile_page.click_on_profile_button()
        assert profile_page.check_profile_page_is_loaded(), 'Страница профиля не загружена'

    @allure.title('Проверка клика по ссылке "Личный кабинет" авторизованного пользователя')
    def test_open_order_history_order_history_opened(self, driver, generate_user_data):
        email, password = generate_user_data
        profile_page = ProfilePage(driver)
        profile_page.set_credentials(email, password)
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_overlay_to_disappear()
        profile_page.click_on_submit_button()
        constructor_page.wait_for_overlay_to_disappear()
        constructor_page.click_on_constructor_link()
        constructor_page.create_test_order()
        constructor_page.press_esc()
        constructor_page.wait_for_overlay_to_disappear()
        profile_page.click_on_profile_button()
        constructor_page.wait_for_overlay_to_disappear()
        profile_page.click_on_order_history_link()
        assert profile_page.check_order_history_is_loaded(), 'История заказов не загружена'

    @allure.title('Проверка клика по кнопке "Выход" авторизованного пользователя')
    def test_click_on_logout_button_form_opened(self, driver, generate_user_data):
        email, password = generate_user_data
        profile_page = ProfilePage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page.set_credentials(email, password)
        constructor_page.wait_for_overlay_to_disappear()
        profile_page.click_on_submit_button()
        constructor_page.wait_for_overlay_to_disappear()
        profile_page.click_on_profile_button()
        constructor_page.wait_for_overlay_to_disappear()
        profile_page.click_on_logout_button()
        assert profile_page.check_user_logged_out(), 'Пользователь не вышел из системы'