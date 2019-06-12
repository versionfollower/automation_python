import pytest
import time
from pages import SingUp
from pages import InitialPage
from drivers import DriverFactory
from drivers import DriverChrome
import sys
sys.path.append("..")

driver = DriverFactory.get_driver("chrome")
driver.instanceDriver()
driverIntanced = driver.returnDriver()
sing_up_page = SingUp(driverIntanced)
initial_page = InitialPage(driverIntanced)


def test_validate_second_page_in_create_account_is_displayed():
    driverIntanced.get("https://twitter.com/")
    initial_page.go_to_sing_up()
    time.sleep(10)
    sing_up_page.fill_first_step_create_account("edwin", "982021870")
    assert sing_up_page.get_text_from_title().find("2")
