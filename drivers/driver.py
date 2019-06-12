from selenium import webdriver
from abc import ABC, abstractstaticmethod,abstractmethod

class IDriver(ABC):

    @abstractmethod
    def instanceDriver(self):
        pass

    @abstractmethod
    def freeDriver(self):
       pass

    @abstractmethod
    def returnDriver(self):
       pass
