import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.customLogger import LogGen

class HiThere_ContinuePages:
    # Hi There! continue first page

    HiThere_Text_xpath = "//android.widget.TextView[@text='Hi there!']"
    EnjoyBikeRide_Text_xpath ="//android.widget.FrameLayout[@content-desc='carousel, content']/android.widget.LinearLayout/android.widget.TextView[2]"
    Image_Display_xpath ="//android.widget.FrameLayout[@content-desc='carousel, content']//android.widget.FrameLayout"
    HiThere_ContinueBtn_xpath = '//android.widget.TextView[@content-desc="Continue, button"]'

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
    def IsDisplayed_Image(self, driver):
           Element = driver.find_element(MobileBy.XPATH, self.Image_Display_xpath)
           Element = Element.is_displyed()
           return Element

    @allure.step
    def ClickOnDontAllow(self, driver):
        try:
            time.sleep(10);
            alert = driver.switch_to.alert
            alert.accept()
            self.logger.info("1st alert accepted")
            print("1st alert accepted")
        except TimeoutException:
            self.logger.info("no alert")
            print("no alert")

            # 2nd alert
        try:
            time.sleep(10);
            alert = driver.switch_to.alert
            alert.accept()
            self.logger.info("2nd alert accepted")
            print("2nd alert accepted")
        except TimeoutException:
            self.logger.info("no alert")
            print("no alert")







#  //android.widget.FrameLayout[@content-desc="carousel, content"]/android.widget.LinearLayout/android.widget.TextView[1]

#  Enjoy your bike ride while staying safe on th eroad. Let's get started.
# //android.widget.FrameLayout[@content-desc="carousel, content"]/android.widget.LinearLayout/android.widget.TextView[2]


# Image view should be display proper
# //android.widget.FrameLayout[@content-desc="carousel, content"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView


#click on continue button
# //android.widget.TextView[@content-desc="Continue, button"]
