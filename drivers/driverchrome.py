from drivers.driver import IDriver
from selenium import webdriver

class DriverChrome(IDriver):

    def __init__(self):
        self.driver =None

    def instanceDriver(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\pc\Desktop\django\chromedriver.exe')

    def freeDriver(self):
        self.driver.quit()
    
    def returnDriver(self):
       return self.driver


