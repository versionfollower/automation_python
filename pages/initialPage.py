

class InitialPage:
    def __init__(self, driver):
        self.driver = driver
        self.sing_up = ".//a[contains(text(),'Sign Up')]"
        self.log_in = "(.//a[contains(text(),'Log in')])[2]"

    def go_to_login_page(self):
        self.driver.find_element_by_xpath(self.log_in).click()

    def go_to_sing_up(self):
        self.driver.find_element_by_xpath(self.sing_up).click()
        
