from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    MAIN_PAGE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    INGREDIENT = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    CLOSE_INGREDIENT_DETAILS_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button")
    ACTIVE_MODAL = (By.CSS_SELECTOR, "section.Modal_modal__P3_V5")
    BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    ORDER_MODAL = (By.XPATH, "//p[text()='идентификатор заказа']")
    CLOSE_ORDER_MODAL_BUTTON = (By.XPATH, "//button[@type='button']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")