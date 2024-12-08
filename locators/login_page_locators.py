from selenium.webdriver.common.by import By


class LoginPageLocators:

    RECOVER_PASSWORD = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//Button[text()='Войти']")
