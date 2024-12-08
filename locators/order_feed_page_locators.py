from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FEED_HEADER = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    ORDER_PREPARATION_MESSAGE = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]")
    ORDER = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    ORDER_DETAILS_WINDOW = (By.XPATH, "//div[contains(@class,'Modal_orderBox__1xWdi')]")
    ORDER_LIST = (By.CSS_SELECTOR, 'ul.OrderFeed_list__OLh59 > li')
    ORDER_LIST_NUMBERS = (By.CSS_SELECTOR, '.text.text_type_digits-default')
    ALL_TIME_COUNTER = (By.XPATH, "//div[p[text()='Выполнено за все время:']]/p[2]")
    TODAY_COUNTER = (By.XPATH, "//div[p[text()='Выполнено за сегодня:']]/p[2]")
    IN_WORK_SECTION = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi")
    IN_WORK_ORDERS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li")
    # ORDER_IN_WORK_LOCATOR = (By.XPATH, "//li[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]")