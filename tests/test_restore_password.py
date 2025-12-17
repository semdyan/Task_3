import allure

from pages.constructor_page import ConstructorPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.profile_page import ProfilePage


class TestRestorePassword:
    @allure.title('Проверка перехода на страницу восстановления пароля по клику на кнопку "Восстановить пароль"')
    def test_click_on_button_forgot_password_page_opened(self, driver):
        profile_page = ProfilePage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        profile_page.open_login_form()
        forgot_password_page.click_forgot_password_link()
        assert forgot_password_page.check_forgot_password_page_loaded(), 'Страница восстановления пароля не загрузилась'

    @allure.title('Проверка перехода на форму ввода пароля по клику на кнопку "Восстановить"')
    def test_set_email_and_click_restore_button_form_opened(self, driver, generate_user_data):
        email = generate_user_data[0]
        profile_page = ProfilePage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        profile_page.open_login_form()
        forgot_password_page.click_forgot_password_link()
        forgot_password_page.set_email_and_submit(email)
        assert forgot_password_page.check_set_new_password_page_loaded(), 'Страница с формой ввода нового пароля не загрузилась'

    @allure.title('Проверка что поле для ввода пароля подсвечивается по клику на иконку "Показать пароль"')
    def test_click_on_show_password_icon_field_highlighted(self, driver, generate_user_data):
        email = generate_user_data[0]
        forgot_password_page = ForgotPasswordPage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page = ProfilePage(driver)
        profile_page.open_login_form()
        forgot_password_page.click_forgot_password_link()
        forgot_password_page.set_email_and_submit(email)
        constructor_page.wait_for_overlay_to_disappear()
        forgot_password_page.click_show_password_icon()
        assert forgot_password_page.check_password_input_border_changed_color(), 'Поле для ввода пароля не подсветилось'
