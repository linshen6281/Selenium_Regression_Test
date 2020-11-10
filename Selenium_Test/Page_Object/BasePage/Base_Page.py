from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, loc):
        by = 0
        if loc[0].upper() == "ID":
            by = By.ID
        el = self.driver.find_element((by, loc[1]))
        return el

    def click(self, loc):
        self.driver.find_element(*loc).click()

    def input_text(self, loc, text):
        self.driver.find_element(*loc).send_keys(text)

    def get_title(self):
        return self.driver.title

    def close(self):
        self.driver.close()




