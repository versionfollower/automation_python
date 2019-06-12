

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sing_up = ".//a[contains(text(),'Sign Up')]"
        self.log_in = "(.//a[contains(text(),'Log in')])[2]"

    def search_page(self, brand):
        self.driver.find_element_by_id("login-password")
        self.driver.find_element_by_id("login-submit")
