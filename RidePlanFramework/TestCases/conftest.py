import time

import allure

from utilities.readProperties import ReadConfig
import pytest
from appium import webdriver

driver = None
@pytest.fixture()
def setup(os):
     Path = ReadConfig.getApplicationPath()
     iOSPath = ReadConfig.getApplicationIOSPath()
     global driver
     if os=="iOS":
         driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4723/wd/hub',
             desired_capabilities={
                 'app': iOSPath,
                 'platformName': 'iOS',
                 'platformVersion': '15.5',
                 'deviceName': 'iphone 11 Pro Max',
                 'udid': 'D1DA87BA-0164-4C15-8F9C-1019D1FDCE1F',
                 'clearSystemFiles': 'true'
             })

     elif os=="android":
        desired_caps = {
           "deviceName": "Emaulator",
           "platformName": "Android",
           "app": Path,
            'clearSystemFiles': 'true'
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
     print('setup for device')
     time.sleep(10)
     return driver






def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--os")


@pytest.fixture()
def os(request):  # This will return the os value to setup method
    return request.config.getoption("--os")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Ride plan'
    config._metadata['Module Name'] = 'Route'
    config._metadata['Tester'] = 'Pooja Salunkhe'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




