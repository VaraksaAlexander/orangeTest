from selenium.webdriver import Keys
from orangeTest.conditions import element, type, click, find_element


class LoginPage:
    def __init__(self):
        self.__username = 'input[name*="username"]'

    def fill_username(self, name):
        if name is not None:
            # self.__username.type(user.name)
            # type('input[name*="username"]', value=name + Keys.ENTER)
            type(self.__username, value=name)
