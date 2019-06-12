from drivers.driverchrome import DriverChrome
from drivers.driverfirefox import DriverFirefox
from drivers.driverIE import DriverIE


class DriverFactory():
    @staticmethod
    def get_driver(browser):
        if browser== "chrome":
            return DriverChrome()
        if browser== "firefox":
            return DriverFirefox()
        if browser== "ie":
            return DriverIE()
        