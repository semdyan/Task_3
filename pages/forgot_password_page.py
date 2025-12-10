import allure

from locators.athorization_locators import AuthFormsLocators, AuthButtonLocators
from pages.base_page import BasePage
from data import Urls


class ForgotPasswordPage(BasePage):
    @allure.step('Переход на форму восстановления пароля')
    def go_to_forgot_password_page(self):
        self.go_to_url(Urls.BASE_URL)
        self.wait_and_click_element(AuthButtonLocators.LOGIN_BUTTON)
        self.wait_and_click_element(AuthButtonLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Ввод почты и переход на форму восстановления пароля')
    def set_email_and_submit(self, email):
        email_input = self.wait_and_get_element(AuthFormsLocators.FORGOT_PASSWORD_EMAIL_INPUT)
        email_input.send_keys(email)
        self.wait_and_click_element(AuthButtonLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('Клик по иконке "Показать пароль"')
    def click_show_password_icon(self):
        self.wait_for_element_to_disappear(AuthFormsLocators.INVISIBLE_OVERLAY)
        self.wait_and_click_element(AuthButtonLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверка перехода на форму восстановления пароля')
    def check_set_new_password_page_loaded(self):
        password_input = self.wait_and_get_element(AuthFormsLocators.FORGOT_PASSWORD_PASSWORD_PLACEHOLDER)
        return password_input.is_displayed()

    @allure.step('Проверка перехода на форму восстановления пароля')
    def check_forgot_password_page_loaded(self):
        email_input = self.wait_and_get_element(AuthFormsLocators.FORGOT_PASSWORD_EMAIL_INPUT)
        return email_input.is_displayed()

    @allure.step('Проверка, что рамка поля для ввода пароля подсвечивается')
    def check_password_input_border_changed_color(self):
        password_input_frame = self.wait_and_get_element(AuthFormsLocators.FORGOT_PASSWORD_PASSWORD_INPUT_FRAME)
        div_class = password_input_frame.get_attribute('class')
        return 'input_status_active' in div_class