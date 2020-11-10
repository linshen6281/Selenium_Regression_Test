from Page_Object.BasePage.Base_Page import BasePage
import configparser
from selenium import webdriver

class LoginPage(BasePage):
    def __init__(self, driver, base_url=None):
        self.initParam()
        super().__init__(driver, base_url)

    def initParam(self, config_file=None):
        if not config_file:
            config_file = "../config/conf.config"
        config = configparser.ConfigParser()
        config.read(config_file, encoding="utf-8")

        self.base_url = config.get("URL", "BASE_URL")
        self.input = config.get("LoginBaiduPage", "baidu_input").split("<")
        self.click = config.get("LoginBaiduPage", "baidu_clikc").split("<")

    def go_to_baidu(self):
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")

    def input_baidu_text(self, text):
        super().input_text(self.input, text)

    def click_baidu(self):
        super().click(self.click)

    def run(self, text):
        self.go_to_baidu()
        print(1)
        self.input_baidu_text(text)
        print(10)
        self.click_baidu()


if __name__ == '__main__':

    driver = webdriver.Chrome()
    Login = LoginPage(driver)
    Login.run("语文")






