

class SingUp:
    def __init__(self, driver):
        self.driver = driver
        self.name = ".//input[@name='name']"
        self.phone = ".//input[@name='phone_number']"
        self.next = ".//span[contains(text(),'Siguiente')]/../../.."

        self.second_step_title = ".//h2/span"

    def fill_first_step_create_account(self, name, phone_number):
        self.driver.find_element_by_xpath(self.name).send_keys(name)
        self.driver.find_element_by_xpath(self.phone).send_keys(phone_number)
        self.driver.find_element_by_xpath(self.next).click()

    def get_text_from_title(self):
        return self.driver.find_element_by_xpath(self.second_step_title).text
