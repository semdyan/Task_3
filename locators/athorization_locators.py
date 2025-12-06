from selenium.webdriver.common.by import By


class ButtonLocators:
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, './/a[text()="Восстановить пароль"]')
    RESTORE_PASSWORD_BUTTON = (By.XPATH, './/button[text()="Восстановить"]')
    SHOW_PASSWORD_ICON = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
    GO_TO_PROFILE_BUTTON = (By.XPATH, './/p[text()="Личный кабинет"]/parent::a')

class AuthFormsLocators:
    FORGOT_PASSWORD_EMAIL_PLACEHOLDER = (By.XPATH, './/label[text()="Email"]')
    FORGOT_PASSWORD_EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    FORGOT_PASSWORD_PASSWORD_PLACEHOLDER = (By.XPATH, './/label[text()="Пароль"]')
    FORGOT_PASSWORD_PASSWORD_INPUT_FRAME = (By.XPATH, './/label[text()="Пароль"]/parent::div')