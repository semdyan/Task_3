from selenium.webdriver.common.by import By


class AuthButtonLocators:
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]') #Кнопка "Войти в аккаунт"
    SUBMIT_BUTTON = (By.XPATH, './/button[text()="Войти"]') #Кнопка "Войти"
    FORGOT_PASSWORD_LINK = (By.XPATH, './/a[text()="Восстановить пароль"]') #Ссылка "Восстановить пароль"
    RESTORE_PASSWORD_BUTTON = (By.XPATH, './/button[text()="Восстановить"]') #Кнопка "Восстановить"
    SHOW_PASSWORD_ICON = (By.XPATH, './/div[@class="input__icon input__icon-action"]') #Иконка "Показать пароль"


class AuthFormsLocators:
    LOGIN_EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/following-sibling::input') #Поле ввода Email
    LOGIN_PASSWORD_INPUT = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input') #Поле ввода пароля
    FORGOT_PASSWORD_EMAIL_PLACEHOLDER = (By.XPATH, './/label[text()="Email"]') #Плейсхолдер Email на форме восстановления пароля
    FORGOT_PASSWORD_EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
                                                                        #Поле ввода Email на форме восстановления пароля
    FORGOT_PASSWORD_PASSWORD_PLACEHOLDER = (By.XPATH, './/label[text()="Пароль"]') #Плейсхолдер пароля на форме восстановления пароля
    FORGOT_PASSWORD_PASSWORD_INPUT_FRAME = (By.XPATH, './/label[text()="Пароль"]/parent::div')
                                                                #Рамка поля ввода пароля на форме восстановления пароля
    INVISIBLE_OVERLAY = (By.XPATH, '//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]')
                                                                                                    #Невидимый оверлей