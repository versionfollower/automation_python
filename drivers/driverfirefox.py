from drivers.driver import IDriver
from selenium import webdriver

class DriverFirefox(IDriver):

    def __init__(self):
        self.driver =None

    def instanceDriver(self):
        self.driver = webdriver.Ie(executable_path=r'C:\Users\pc\Desktop\django\iedriver.exe')

    def freeDriver(self):
        self.driver.quit()
    
    def returnDriver(self):
       return self.driver


