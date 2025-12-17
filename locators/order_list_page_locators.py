from selenium.webdriver.common.by import By

class OrderListPageLocators:
    ORDER_FEED = (By.XPATH, ".//div[@class='OrderFeed_orderFeed__2RO_j']") #Список заказов в Ленте заказов
    ORDER_DETAILS_MODAL = (By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
                                                                                       #Модальное окно с деталями заказа
    ORDERS_LIST_IN_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']/p[@class='text text_type_digits-default']")
                                                                                        #Список заказов в Ленте заказов
    TODAYS_SUCCESSFUL_ORDERS_COUNT = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p')
                                                                                #Количество успешных заказов за сегодня
    TOTAL_SUCCESSFUL_ORDERS_COUNT = (By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p')
                                                                                    #Общее количество успешных заказов
    ORDERS_IN_WORK_LIST = (By.XPATH, ".//div[@class='OrderFeed_orderStatusBox__1d4q2 mb-15']/"
                                    "ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")
                                                                                                #Список заказов в работе