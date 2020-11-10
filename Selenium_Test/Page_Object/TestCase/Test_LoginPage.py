import time
import unittest
from ddt import ddt, data
from Page_Object.Page.LoginPage import LoginPage
from selenium import webdriver

@ddt
class TestCase_Login(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    @data("Chines", "English")
    def test_login(self, text):
        loginPage = LoginPage(self.driver)
        loginPage.run(text)
        print(text)
        time.sleep(2)
        self.assertEqual(loginPage.get_title(), "text" + "_百度搜索")


    def tearDown(self):
        self.driver.close()



