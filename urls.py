# urls.py
class URLs:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTER_PAGE = f'{BASE_URL}register'
    LOGIN_PAGE = f'{BASE_URL}login'
    FORGOT_PASS_PAGE = f'{BASE_URL}forgot-password'
    RESET_PASS_PAGE = f'{BASE_URL}reset-password'
    PERSONAL_ACCOUNT_PAGE = f'{BASE_URL}account/profile'
    ORDER_HISTORY_PAGE = f'{BASE_URL}account/order-history'
    ORDER_PAGE = f'{BASE_URL}feed'

# API endpoints
class UrlsAPi:
    BASE_API_URL = 'https://stellarburgers.nomoreparties.site/api/'
    CREATE_USER = f'{BASE_API_URL}auth/register'
    DELETE_USER = f'{BASE_API_URL}auth/user'
