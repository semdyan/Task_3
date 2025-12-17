from selenium.webdriver.common.by import By

class ProfilePageElementsLocators:
    PROFILE_LINK = (By.XPATH, './/a[text()="Профиль"]') #Ссылка на страницу профиля в хэддере
    ORDER_HISTORY_LINK = (By.XPATH, './/a[text()="История заказов"]') #Ссылка историю заказов в профиле
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]') #Кнопка выхода из профиля
    ORDER_HISTORY_LIST = (By.XPATH, './/div[@class="OrderHistory_orderHistory__qy1VB"]') #Список заказов в профиле
    ORDERS_LIST_IN_PROFILE = (By.XPATH, './/div[@class="OrderHistory_textBox__3lgbs mb-6"]'
                                        '/p[@class="text text_type_digits-default"]') #Список заказов в профиле

class ProfilePageButtonsLocators:
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]') #Кнопка "Войти в аккаунт"
    SUBMIT_BUTTON = (By.XPATH, './/button[text()="Войти"]') #Кнопка "Войти"
    GO_TO_PROFILE_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]') #Кнопка "Личный кабинет" в хэддере

class ProfileAuthInputLocators:
    LOGIN_EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/following-sibling::input') #Поле ввода Email
    LOGIN_PASSWORD_INPUT = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input') #Поле ввода пароля