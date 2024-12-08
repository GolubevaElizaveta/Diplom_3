from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Профиль')]")
    LOGIN_TITLE_LOCATOR = (By.XPATH, "//h2[text()='Вход']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    LAST_ORDER_NUMBER = (By.XPATH, """
        //li[@class='OrderHistory_listItem__2x95r mb-6'][last()]
        //p[@class='text text_type_digits-default']
    """)