from selenium.webdriver.common.by import By


class ForgotPasswordButtonLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, './/a[text()="Восстановить пароль"]') #Ссылка "Восстановить пароль"
    RESTORE_PASSWORD_BUTTON = (By.XPATH, './/button[text()="Восстановить"]') #Кнопка "Восстановить"
    SHOW_PASSWORD_ICON = (By.XPATH, './/div[@class="input__icon input__icon-action"]') #Иконка "Показать пароль"


class ForgotPasswordFormsLocators:
    FORGOT_PASSWORD_EMAIL_PLACEHOLDER = (By.XPATH, './/label[text()="Email"]') #Плейсхолдер Email на форме восстановления пароля
    FORGOT_PASSWORD_EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
                                                                        #Поле ввода Email на форме восстановления пароля
    FORGOT_PASSWORD_PASSWORD_PLACEHOLDER = (By.XPATH, './/label[text()="Пароль"]') #Плейсхолдер пароля на форме восстановления пароля
    FORGOT_PASSWORD_PASSWORD_INPUT_FRAME = (By.XPATH, './/label[text()="Пароль"]/parent::div')
                                                                #Рамка поля ввода пароля на форме восстановления пароля
