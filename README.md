# Task_3
UI-tests

## В проекте организована структура файлов и директорий POM:
### locators - директория с локаторами 
- authorization_locators - локаторы, которые используются в процессе авторизации
- main_page_locators - локаторы элементов главной страницы / страницы с конструктором
- order_list_page_locators - локаторы элементов страницы "Лента заказов"
- profile_page_locators - локаторы элементов личного кабинета

### pages - директория с файлами POM 
- base_page:
  - go_to_url - прямой переход по URL
  - wait_for_element_to_disappear - ожидание, пока перестанет отображаться элемент
  - wait_and_get_element - ождание и получение элемента по локатору
  - wait_and_get_elements - ожидание и получение нескольких элементов по локатору
  - wait_and_click_element - ожидание и клик по элементу
  - wait_until_text_changes - ожидание смены текста элемента
  - set_field - заполнение поля по локатору
  - scroll_to_element_by_element - скролл до элемента
  - press_esc - имитация нажатия на esc

- constructor_page:
  - open_constructor_page - прямой переход на главную страницу / страницу конструктора
  - click_on_constructor_link - клик по ссылке "Конструктор" в хэддере
  - return_random_ingredient - получение произвольного ингредиента
  - click_on_close_ingredient_details_button - клик по кнопке закрытия модального окна "Детали ингредиента"
  - add_test_burger_to_basket - создание произвольного бугрера в конструкторе
  - drag_and_drop_to_basket - перетаскивание ингредиента в корзину
  - click_on_confirm_order_button - клик по кнопке "Оформить заказ
  - return_order_number - получение номера оформленного заказа
  - create_test_order - создание тестового заказа
  - check_constructor_page_loaded - проверка загрузки главной страницы / страницы конструктора
  - check_ingredient_details_opened - проверка, что открылось модальное окно "Детали ингредиента"
  - check_ingredient_details_closed - проверка, что закрылось модальное окно "Детали ингредиента"
  - get_basket_counter_value - получение значения счетчика цены в конструкторе

- forgot_password_page:
  - go_to_forgot_password_page - переход на форму восстановления пароля
  - set_email_and_submit - ввод почты и переход на форму восстановления пароля
  - click_show_password_icon - клик по иконке "Показать пароль"
  - check_set_new_password_page_loaded - проверка перехода на форму восстановления пароля
  - check_forgot_password_page_loaded - проверка перехода на форму восстановления пароля
  - check_password_input_border_changed_color - проверка, что рамка поля для ввода пароля подсвечивается

- order_list_page:
  - go_to_order_list_page - переход на страницу "Лента заказов"
  - click_on_order_list_link - нажатие на ссылку "Лента заказов" в хэддере
  - get_random_order_from_list - выбор и возврат произвольного заказа из списка
  - get_feed_orders_numbers_list - получение номеров заказов из ленты заказов
  - missing_profile_orders_in_feed - проверка, что заказы из профиля есть в ленте заказов
  - get_todays_successful_orders - получение значения счетчика выполненных сегодня заказов
  - get_total_successful_orders - получение значения счетчика всех выполненных заказов
  - get_orders_in_work_list - получение списка заказов в работе
  - wait_for_in_work_list_refresh - ожидание обновления списка "В работе"
  - check_order_details_opened - проверка, что открылись детали заказа
  - check_order_list_page_loaded - проверка загрузки страницы "Лента заказов"

- profile_page:
  - login_user - авторизация пользователя
  - click_on_profile_button - клик по кнопке "Профиль"
  - click_on_order_history_link - клик по кнопке "История заказов"
  - click_on_logout_button - клик по кнопке "Выход"
  - get_profile_orders_numbers_list - получение номеров заказов из профиля
  - check_order_history_is_loaded - проверка загрузки истории заказов
  - check_profile_page_is_loaded - проверка загрузки страницы профиля
  - check_user_logged_out - проверка выхода из профиля
  
### tests - директория с файлами тестов
- test_constructor.py - файл с тестами главной страницы / страницы конструктора
  TestConstructorPage - класс с тестами страницы конструктора
  - test_click_on_constructor_link_constructor_page_loaded - проверка клика по ссылке "Конструктор"
  - test_click_on_random_ingredient_details_loaded - проверка клика по случайному ингредиенту
  - test_click_on_close_ingredient_details_button_details_closed - оверка клика по кнопке закрытия деталей ингредиента
  - test_add_ingredient_to_order_counter_changed - проверка изменения каунтера при добавлении ингредиента в заказ
  - test_confirm_order_authorized_user_order_placed - проверка успешного заказа авторизованным пользователем

- test_order_list.py - файл с тестами ленты заказов
  TestOrderListPage - класс с тестами ленты заказов
  - test_click_on_constructor_link_constructor_page_opened - проверка клика по ссылке "Конструктор"
  - test_check_order_details_displayed - проверка отображения деталей заказа
  - test_check_user_orders_displayed_in_order_list - проверка, что заказы пользователя отображаются в списке
  - test_todays_successful_orders_counter_updates_on_new_order - проверка, что счетчик выполненных заказов за сегодня 
    обновляется при создании нового заказ
  - test_total_successful_orders_counter_updates_on_new_order - проверка, что счетчик выполненных заказов за все время 
    обновляется при создании нового заказа
  - test_order_number_in_making_list - проверка, что номер заказа появляется в списке "В работе"

- test_profile.py - файл с тестами личного кабинета
  TestProfilePage - класс с тестами личного кабинета
  - test_click_on_profile_button_authorized_user_profile_opened - проверка клика по ссылке "Личный кабинет" 
    авторизованного пользователя
  - test_open_order_history_order_history_opened - проверка клика по ссылке "Личный кабинет" авторизованного пользователя
  - test_click_on_logout_button_form_opened - проверка клика по кнопке "Выход" авторизованного пользователя

- test_restore_password - с тестами сценария восстановления пароля
  TestRestorePassword - класс с тестами сценария восстановления пароля
  - test_click_on_button_forgot_password_page_opened - поверка перехода на страницу восстановления пароля по клику 
    на кнопку "Восстановить пароль"
  - test_set_email_and_click_restore_button_form_opened - проверка перехода на форму ввода пароля по клику 
    на кнопку "Восстановить"
  - test_click_on_show_password_icon_field_highlighted - проверка что поле для ввода пароля подсвечивается по клику 
    на иконку "Показать пароль"
  
## conftest.py - файл с фикстурами
- driver - генерирует драйвер по параметрам
- generate_user_data - генерирует и возвращает данные пользователя, затем удаляет созданного пользователя

## conftest.py - файл со вспомогательными функциями
- create_and_return_user - регистрирует пользователя и возвращает данные для авторизации
- login_and_delete_user - удаляет созданного ранее пользователя

## data.py - файл с данными для тестов
- Urls - класс с адресами

## requirements.txt - файл с необходимыми импортами