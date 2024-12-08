import allure
from page_objects.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators



class RecoverPasswordPage(BasePage):

    @allure.step("Вводим email")
    def input_email(self, email):
        self.add_text_to_element(RecoveryPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step("Нажатие на кнопку 'Восстановить'")
    def click_on_recover_button(self, url):
        recover_button = self.find_element_with_wait(RecoveryPasswordPageLocators.RECOVER_BUTTON)
        self.click_on_element_js(recover_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Проверка отображения пароля при нажатии на 'Глаз'")
    def click_on_view_password(self):
        VIEW_PASSWORD = self.find_element_with_wait(RecoveryPasswordPageLocators.VIEW_PASSWORD)
        self.click_on_element_js(VIEW_PASSWORD)

    @allure.step("Проверка видимости пароля")
    def is_password_visible(self):
        password_input = self.find_element_with_wait(RecoveryPasswordPageLocators.RESET_PASSWORD_INPUT)
        return password_input.get_attribute('type') == 'text'

    def is_recovery_password_header_visible(self):
        """Проверяет, виден ли заголовок 'Восстановление пароля' на странице."""
        try:
            header = self.find_element_with_wait(RecoveryPasswordPageLocators.HEADER_RECOVERY_PASSWORD)
            return header.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
