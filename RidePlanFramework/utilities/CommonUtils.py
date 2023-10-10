import allure
import softest
from allure_commons.types import AttachmentType
import time

from selenium.common import TimeoutException

from Android_PageObjects.Android_HiThere_ContinuePage import HiThere_ContinuePages
from utilities.customLogger import LogGen

class CommonMethods(softest.TestCase):
    logger = LogGen.loggen()

    @allure.step
    def tear_down(self, driver):
        time.sleep(10)
        print('Quit the driver')
        driver.quit()

    @allure.step
    def TryExpectBlockfor_TextMatch(self, driver, Actual_Result, Expected_Result):

        try:
            assert Actual_Result == Expected_Result
            self.logger.info("Text is match--> Expected Result: " + Expected_Result + "---||--- Actual Result : "+Actual_Result)
            print("Text is match--> Expected Result: " + Expected_Result + "---||--- Actual Result : "+Actual_Result)

        except AssertionError:
            self.logger.error("Assertion failed. --> Expected Result: "+ Expected_Result + "---||--- Actual Result : "+Actual_Result)
            print("Assertion failed. Expected Result: " + Expected_Result + "---||--- Actual Result : "+Actual_Result)
            allure.attach(driver.get_screenshot_as_png(), name="AssertionFail", attachment_type=AttachmentType.PNG)
            assert False

    @allure.step
    def TryExpectBlockfor_Isdisplayed(self, driver, Element, Message):
            try:
                    if Element == True:
                      self.logger.info(Message+ " --> Displayed")
                      print(Message+" --> Displayed")
            except:
                    driver.save_screenshot("./Screenshots/" + "isdisplyed.png")
                    self.logger.error(Message+ " --> Assertion failed")
                    print(Message+ " --> Assertion failed")
                    allure.attach(driver.get_screenshot_as_png(), name="AssertionFail",
                                  attachment_type=AttachmentType.PNG)
                    assert False

    #Click on Onboarding pages
    @allure.step
    def OnboardingPages(self, driver):
            self.Hithere = HiThere_ContinuePages()
            # Click on continue button
            self.Hithere.clickOnContinueBtn(driver)
            self.Hithere.clickOnContinueBtn(driver)
            self.Hithere.clickOnContinueBtn(driver)
            self.Hithere.clickOnContinueBtn(driver)

            # 1st alert
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





