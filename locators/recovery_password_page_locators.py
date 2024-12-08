from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    VIEW_PASSWORD = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    RESET_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    HEADER_RECOVERY_PASSWORD = (By.XPATH, "//h2[text()='Восстановление пароля']")

