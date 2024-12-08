import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы по URL")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента с ожиданием")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step("Поиск элементов с ожиданием")
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу с использованием JavaScript")
    def click_on_element_js(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Добавление текста в элемент")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста из элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание перехода на указанный URL")
    def wait_for_url_to_be(self, url):
        WebDriverWait(self.driver, 20).until(
            EC.url_to_be(url)
        )

    @allure.step("Ожидание изменения текста элемента")
    def wait_for_text_to_change(self, locator, initial_value):
        WebDriverWait(self.driver, 20).until(
            lambda driver: self.get_text_from_element(locator) != initial_value
        )

    @allure.step("Перемещение элементов")
    def move_elements(self, source, target):
        return drag_and_drop(self.driver, source, target)
