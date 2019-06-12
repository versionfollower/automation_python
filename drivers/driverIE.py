from drivers.driver import IDriver
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

class DriverIE(IDriver):

    def __init__(self):
        self.driver =None

    def instanceDriver(self):
        self.driver = webdriver.Ie(executable_path=r'C:\Users\pc\Desktop\django\iedriver.exe')
        #return driver

    #def freeDriver(self,driver):
    def freeDriver(self):
        self.driver.quit()
    
    def returnDriver(self):
       return self.driver


