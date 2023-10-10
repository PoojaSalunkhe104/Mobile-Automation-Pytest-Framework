import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.customLogger import LogGen

class iOS_HiThere_ContinuePages:
    # Hi There! continue first page

    HiThere_Text_xpath = "//XCUIElementTypeStaticText[@name='Hi there!']"
    EnjoyBikeRide_Text_xpath ="//XCUIElementTypeStaticText[@name='Enjoy your bike ride while ']"
    HiThere_ContinueBtn_xpath = "//XCUIElementTypeStaticText[@name='Continue']"
    AllowOnce='Allow Once'
    DontAllow="Don’t Allow"

    HiThere_Text = ''
    logger = LogGen.loggen()

    def _init__(self, driver):
        self.driver = driver

#click on continue button
    @allure.step
    def clickOnContinueBtn(self, driver):
         Btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, self.HiThere_ContinueBtn_xpath))
         )
         Btn.click()
         self.logger.info("Clicked on Continue Button")
         print("Clicked on Continue Button")


#  verify Hi there! Text
    @allure.step
    def GetText_HiThere(self, driver):
           HiThere_Text = driver.find_element(MobileBy.XPATH, self.HiThere_Text_xpath)
           HiThere_Text = HiThere_Text.text
           return HiThere_Text

# Verify Enjoy bike ride Text is displayed
    @allure.step
    def IsDisplayed_BikeRideText(self, driver):
           Element = driver.find_element(MobileBy.XPATH, self.EnjoyBikeRide_Text_xpath)
           Element = Element.is_displayed()
           return Element

    @allure.step
    def ClickOnAllowOnce(self, driver):
        Btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, self.AllowOnce))
        )
        Btn.click()
        print("Clicked on Allow Once Button")
        self.logger.info("Clicked on Allow Once Button")

    @allure.step
    def ClickOnDontAllow(self, driver):
        Btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, self.DontAllow))
        )
        Btn.click()
        print("Clicked on Don't Allow Button")
        self.logger.info("Clicked on Don't Allow Button")













