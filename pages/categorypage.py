from selenium.webdriver.common.by import By

class CategoryPage:

    def __init__(self,driver):
        self.driver = driver


    def check_monitors_count(self,count):
        monitors_count = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors_count) == count