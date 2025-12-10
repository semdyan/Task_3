import allure
import random

from locators.athorization_locators import AuthFormsLocators
from pages.base_page import BasePage
from data import Urls
from locators.main_page_locators import MainPageButtonLocators, ConstructorLocators

class ConstructorPage(BasePage):
    @allure.step('Открытие страницы конструктора')
    def open_constructor_page(self):
        self.go_to_url(Urls.BASE_URL)

    @allure.step('Переход кнопке "Конструктор"')
    def click_on_constructor_link(self):
        self.wait_for_element_to_disappear(AuthFormsLocators.INVISIBLE_OVERLAY)
        self.wait_and_click_element(MainPageButtonLocators.CONSTRUCTOR_LINK)

    @allure.step('Выбор и возврат случайного ингредиента')
    def return_random_ingredient(self):
        ingredients_list = self.wait_and_get_elements(ConstructorLocators.INGREDIENTS_LIST)
        ingredient = ingredients_list[random.randint(0, 10)]
        return ingredient

    @allure.step('Клик по кнопке закрытия модального окна "Детали ингредиента"')
    def click_on_close_ingredient_details_button(self):
        self.wait_and_click_element(ConstructorLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Сборка тестового бургера в корзине')
    def add_test_burger_to_basket(self):
        ingredients_list = self.wait_and_get_elements(ConstructorLocators.INGREDIENTS_LIST)
        bun = ingredients_list[random.randint(0, 1)]
        sauce = ingredients_list[random.randint(2, 5)]
        main = ingredients_list[random.randint(6, len(ingredients_list) - 1)]
        self.drag_and_drop_to_basket(bun)
        self.drag_and_drop_to_basket(sauce)
        self.drag_and_drop_to_basket(main)

    @allure.step('Перетаскивание ингредиента в корзину')
    def drag_and_drop_to_basket(self, source_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);

                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        basket = self.wait_and_get_element(ConstructorLocators.CONSTRUCTOR_BASKET)
        self.driver.execute_script(script, source_element, basket)

    @allure.step('Клик по кнопке "Оформить заказ')
    def click_on_confirm_order_button(self):
        self.wait_and_click_element(MainPageButtonLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверка, что заказу присвоен номер')
    def return_order_number(self):
        self.wait_until_text_changes(ConstructorLocators.ORDER_NUMBER_IN_MODAL, '9999')
        number = self.wait_and_get_element(ConstructorLocators.ORDER_NUMBER_IN_MODAL)
        return number.text

    @allure.step('Оформление заказа')
    def create_test_order(self):
        self.add_test_burger_to_basket()
        self.click_on_confirm_order_button()
        return self.return_order_number()

    @allure.step('Проверка, что загрузилась страница с конструктором')
    def check_constructor_page_loaded(self):
        constructor_basket = self.wait_and_get_element(ConstructorLocators.CONSTRUCTOR_BASKET)
        return constructor_basket.is_displayed()

    @allure.step('Проверка, что открылось модальное окно "Детали ингредиента"')
    def check_ingredient_details_opened(self):
        ingredient_details = self.wait_and_get_element(ConstructorLocators.INGREDIENT_DETAILS)
        return ingredient_details.is_displayed()

    @allure.step('Проверка, что модальное окно "Детали ингредиента" закрылось')
    def check_ingredient_details_closed(self):
        ingredient_details = self.wait_and_get_element(ConstructorLocators.INGREDIENT_DETAILS)
        if ingredient_details:
            self.wait_for_element_to_disappear(ConstructorLocators.INGREDIENT_DETAILS)
        return not ingredient_details.is_displayed()

    @allure.step('Получение значения счетчика ингредиентов в корзине')
    def get_basket_counter_value(self):
        return self.wait_and_get_element(ConstructorLocators.BASKET_COUNTER).text


