class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    CREATE_USER = '/auth/register'
    LOGIN_USER = '/auth/login'
    DATA_USER = '/auth/user'
    TOKEN = '/auth/token'
    ORDER = '/orders'
    GET_ALL_ORDERS = '/orders/all'
    INGRIDIENTS_URL = '/ingredients'


class ID:
    NON_EXISTENT_ID = 'non_existent_id_12345'


class Messages:
    ERROR_403_DUBLICATE = 'User already exists'
    ERROR_403_WITHOUT_DATE = 'Email, password and name are required fields'
    ERROR_401_AUTHORIZED = 'email or password are incorrect'
    ERROR_401_AUTHORIZED_FOR_ORDER_LIST = 'You should be authorised'
    ERROR_403_EMAIL_ALREADY_EXISTS = 'User with such email already exists'
    MESSAGE_SUCCESSFULLY_REMOVED: str = 'User successfully removed'
