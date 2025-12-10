import allure

from pages.forgot_password_page import ForgotPasswordPage

class TestRestorePassword:
    @allure.title('Проверка перехода на страницу восстановления пароля по клику на кнопку "Восстановить пароль"')
    def test_click_on_button_forgot_password_page_opened(self, driver):
        page = ForgotPasswordPage(driver)
        page.go_to_forgot_password_page()
        assert page.check_forgot_password_page_loaded(), 'Страница восстановления пароля не загрузилась'

    @allure.title('Проверка перехода на форму ввода пароля по клику на кнопку "Восстановить"')
    def test_set_email_and_click_restore_button_form_opened(self, driver, generate_user_data):
        email = generate_user_data[0]
        page = ForgotPasswordPage(driver)
        page.go_to_forgot_password_page()
        page.set_email_and_submit(email)
        assert page.check_set_new_password_page_loaded(), 'Страница с формой ввода нового пароля не загрузилась'

    @allure.title('Проверка что поле для ввода пароля подсвечивается по клику на иконку "Показать пароль"')
    def test_click_on_show_password_icon_field_highlighted(self, driver, generate_user_data):
        email = generate_user_data[0]
        page = ForgotPasswordPage(driver)
        page.go_to_forgot_password_page()
        page.set_email_and_submit(email)
        page.click_show_password_icon()
        assert page.check_password_input_border_changed_color(), 'Поле для ввода пароля не подсветилось'
