from selenium.webdriver.common.by import By


class MainPageButtonLocators:
    LOGIN_BUTTON = (By.XPATH, './/button[text="Войти в аккаунт"]') #Кнопка "Войти в аккаунт" в хэддере
    GO_TO_PROFILE_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]') #Кнопка "Личный кабинет" в хэддере
    CONSTRUCTOR_LINK = (By.XPATH, './/p[text()="Конструктор"]') #Кнопка "Конструктор" в хэддере
    ORDER_LIST_LINK = (By.XPATH, './/p[text()="Лента Заказов"]') #Кнопка "Лента заказов" в хэддере
    CONFIRM_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]') #Кнопка "Оформить заказ"

class ConstructorLocators:
    INGREDIENTS_LIST = (By.XPATH, './/p[@class="BurgerIngredient_ingredient__text__yp3dH"]') #Список ингредиентов
    INGREDIENT_DETAILS = (By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]') #Детали ингредиента
    CLOSE_INGREDIENT_DETAILS_BUTTON = (By.XPATH,
                                       './/section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button')
    #Кнопка закрытия деталей ингредиента
    CONSTRUCTOR_BASKET = (By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]') #Корзина конструктора
    BASKET_COUNTER = (By.XPATH, './/p[@class="text text_type_digits-medium mr-3"]') #Счетчик цены в конструкторе
    ORDER_NUMBER_IN_MODAL = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    #Номер заказа в модальном окне
    CLOSE_ORDER_MODAL_BUTTON = (By.CLASS_NAME, 'Modal_modal__close_modified__3V5XS') #Кнопка закрытия модального окна заказа
