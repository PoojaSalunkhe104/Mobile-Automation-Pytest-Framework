import time
import allure
import pytest
import self
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException

from iOS_PageObjects.iOS_HiThere_ContinuePage import iOS_HiThere_ContinuePages
from utilities.CommonUtils import CommonMethods
from utilities.ExcelTestcase import ReadExcelFile
from utilities.customLogger import LogGen
from Android_PageObjects.Android_HiThere_ContinuePage import HiThere_ContinuePages
from utilities.iOSCommonUtils import iOS_CommonMethods

TestCaseName="Test_001_VerifyStartingPages"

class Test_001_VerifyStartingPages():

    logger = LogGen.loggen()

    @allure.step
    def test_VerifycontinuePages(self, setup, os):

        self.logger.info("**** Test case ID 001 VerifyStartingPages Testcase started****")
        print("**** Test case ID 001 VerifyStartingPages Testcase started****")

        #Create object for classes
        self.driver = setup
        self.Excel = ReadExcelFile()

        if os == "iOS":
            self.Hithere = iOS_HiThere_ContinuePages()
            self.commonMethod = iOS_CommonMethods()
            print("Testcase Run on iOS")

        elif os == "android":
            self.Hithere = HiThere_ContinuePages()
            self.commonMethod = CommonMethods()
            print("Testcase Run on android")


        #Reading excelSheet
        Address, Name = self.Excel.readExcelData(self.driver,TestCaseName)

        #Verify Hi There! Text
        time.sleep(10)
        Actual_Result = self.Hithere.GetText_HiThere(self.driver)
        Expected_Result = "Hi there!"
        self.commonMethod.TryExpectBlockfor_TextMatch(self.driver, Actual_Result, Expected_Result)

        #verify Bike ride element is displayed
        Element = self.Hithere.IsDisplayed_BikeRideText(self.driver)
        Message = "Verify Bike ride Text "
        self.commonMethod.TryExpectBlockfor_Isdisplayed(self.driver, Element, Message)

      #Click on continue button
        self.Hithere.clickOnContinueBtn(self.driver)
        self.Hithere.clickOnContinueBtn(self.driver)
        self.Hithere.clickOnContinueBtn(self.driver)
        self.Hithere.clickOnContinueBtn(self.driver)

        self.Hithere.ClickOnDontAllow(self.driver)

        #Close the driver
        self.commonMethod.tear_down(self.driver)








