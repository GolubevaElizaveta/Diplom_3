import allure
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from page_objects.login_page import LoginPage
from urls import URLs


class TestMainPage:

    @allure.title('Переход на страницу "Лента заказов"')
    def test_redirect_to_order_feed_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_page(URLs.BASE_URL)
        actual_url = main_page.click_on_order_feed_button(URLs.ORDER_PAGE)
        assert actual_url == URLs.ORDER_PAGE and order_page.is_order_feed_header_visible(), \
            f"Expected URL: {URLs.ORDER_PAGE}, but got: {actual_url}. " \
            f"Заголовок 'Лента заказов' не найден."

    @allure.title('Переход на страницу "Конструктор"')
    def test_redirect_to_constructor_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_button(URLs.ORDER_PAGE)
        actual_url = main_page.click_on_constructor_button(URLs.BASE_URL)
        assert actual_url == URLs.BASE_URL and main_page.is_constructor_header_visible(), \
            f"Expected URL: {URLs.BASE_URL}, but got: {actual_url}. Заголовок не виден."


    @allure.title('Клик на ингредиент вызывает всплывающее окно с деталями')
    def test_ingredient_details_window_opens_on_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_window_visible = main_page.is_ingredient_details_window_visible()
        assert ingredient_window_visible and main_page.is_ingredient_details_window_visible(), \
            "Окно деталей ингредиента не отображается или заголовок неверный."

    @allure.title('Закрытие окна с деталями ингредиента')
    @allure.description('При клике на кнопку "Закрыть" окно с деталями ингредиента закрывается')
    def test_closing_ingredient_details_window(self, driver):  # Исправлено название теста
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        is_modal_closed = main_page.close_ingredient_details_window()
        assert is_modal_closed, "Ошибка: Окно деталей ингредиента не было закрыто."

    @allure.title('Добавление ингредиента в корзину увеличивает счетчик ингредиента')
    @allure.description('При добавлении ингредиента в корзину счетчик ингредиента увеличивается')
    def test_ingredient_added_increases_basket_counter(self, driver):  # Новое название теста
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        counter_increased = main_page.is_ingredient_counter_increased()
        assert counter_increased, "Ошибка: Счетчик ингредиента не увеличился после добавления в корзину."

    @allure.title('Оформление заказа авторизованным пользователем')
    @allure.description(
        'После добавления ингредиента и нажатия кнопки "Оформить заказ" проверяем, что заказ оформлен и появился идентификатор заказа')
    def test_order_creation_success(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        # Авторизация пользователя
        main_page.click_on_login_button()
        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        # Ожидание загрузки главной страницы
        main_page.wait_for_main_page_to_load()

        # Добавление ингредиента в заказ
        main_page.add_ingredient_to_order()

        # Клик на кнопку "Оформить заказ"
        main_page.click_on_submit_order_button()

        # Проверка, что окно заказа отображается и идентификатор заказа виден
        order_id_visible = main_page.order_window_is_visible()
        order_id_text = main_page.get_order_number()

        assert order_id_visible and order_id_text is not None, \
            f"Окно заказа не отображается или идентификатор заказа неверный: {order_id_text}."