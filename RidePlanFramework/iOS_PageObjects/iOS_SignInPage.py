import allure
import keyboard
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.customLogger import LogGen
import pyautogui


class iOS_Sign_InPage:

    GuestButton = "//XCUIElementTypeButton[@name='continue-as-guest-button']"
    TextSearch = "//XCUIElementTypeApplication[@name='ridePlan-Stage']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField"
    MelbourneLocation = "Melbourne Central"
    WhereToBtn = "//XCUIElementTypeApplication[@name='ridePlan-Stage']/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField"
    RouteButton = "//XCUIElementTypeButton[@name='ROUTE']"
    logger = LogGen.loggen()

    def _init__(self, driver):
        self.driver = driver

#Click on Guest button
    @allure.step
    def SignIn_Guest_Btn(self, driver):
        Btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, self.GuestButton)))
        Btn.click()
        print("Sign In with Guest Button")

        # Click on where to
    @allure.step
    def WhereTo_Btn(self, driver):
        Btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, self.WhereToBtn)))
        Btn.click()
        print("Click on Where To function")

            # Click on where to

    @allure.step
    def TextSearchTab(self, driver, Address):
        Btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, self.TextSearch)))
        Btn.click()
        Btn.send_keys(Address)
        time.sleep(5)
        locationBtn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, self.MelbourneLocation)))
        locationBtn.click()
        time.sleep(5)
        print("Send Address in Text search: "+Address)

#Click on route button
    @allure.step
    def Route_Btn(self, driver):
        Btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, self.RouteButton)))
        Btn.click()
        print("Click on Route Button")


