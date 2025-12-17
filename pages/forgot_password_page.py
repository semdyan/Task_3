import allure

from locators.forgot_password_locators import ForgotPasswordFormsLocators, ForgotPasswordButtonLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step('Переход на форму восстановления пароля')
    def click_forgot_password_link(self):
        self.wait_and_click_element(ForgotPasswordButtonLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Ввод почты и переход на форму восстановления пароля')
    def set_email_and_submit(self, email):
        email_input = self.wait_and_get_element(ForgotPasswordFormsLocators.FORGOT_PASSWORD_EMAIL_INPUT)
        email_input.send_keys(email)
        self.wait_and_click_element(ForgotPasswordButtonLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('Клик по иконке "Показать пароль"')
    def click_show_password_icon(self):
        self.wait_and_click_element(ForgotPasswordButtonLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверка перехода на форму восстановления пароля')
    def check_set_new_password_page_loaded(self):
        password_input = self.wait_and_get_element(ForgotPasswordFormsLocators.FORGOT_PASSWORD_PASSWORD_PLACEHOLDER)
        return password_input.is_displayed()

    @allure.step('Проверка перехода на форму восстановления пароля')
    def check_forgot_password_page_loaded(self):
        email_input = self.wait_and_get_element(ForgotPasswordFormsLocators.FORGOT_PASSWORD_EMAIL_INPUT)
        return email_input.is_displayed()

    @allure.step('Проверка, что рамка поля для ввода пароля подсвечивается')
    def check_password_input_border_changed_color(self):
        password_input_frame = self.wait_and_get_element(ForgotPasswordFormsLocators.FORGOT_PASSWORD_PASSWORD_INPUT_FRAME)
        div_class = password_input_frame.get_attribute('class')
        return 'input_status_active' in div_class