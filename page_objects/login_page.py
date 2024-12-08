from page_objects.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    @allure.step("Клик на кнопку 'Восстановить пароль'")
    def click_on_recover_password_button(self):
        recovery_button = self.find_element_with_wait(LoginPageLocators.RECOVER_PASSWORD)
        self.click_on_element_js(recovery_button)
        actual_url = self.get_current_url()
        return actual_url

    @allure.step("Ввести логин")
    def input_login(self, email):
        email_input = self.find_element_with_wait(LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    @allure.step("Ввести пароль")
    def input_password(self, password):
        password_input = self.find_element_with_wait(LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

    @allure.step("Клик на кнопку 'Войти'")
    def click_on_login_submit_button(self):
        login_button = self.wait_for_element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        self.click_on_element_js(login_button)