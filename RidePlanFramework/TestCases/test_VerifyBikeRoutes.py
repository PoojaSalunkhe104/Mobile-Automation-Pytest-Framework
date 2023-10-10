import allure

from Android_PageObjects.Android_SignInPage import Sign_InPage
from iOS_PageObjects.iOS_SignInPage import iOS_Sign_InPage
from utilities.CommonUtils import CommonMethods
from utilities.ExcelTestcase import ReadExcelFile
from utilities.customLogger import LogGen
from utilities.iOSCommonUtils import iOS_CommonMethods

TestCaseName="Test002_VerifyBikeRoutesPolyline"

class Test002_VerifyBikeRoutesPolyline():
    logger = LogGen.loggen()

    @allure.step
    def test_Verify_BikeRoutes(self, setup, os):
        self.logger.info("**** Test case ID 002 Verify Bike Routes polyline Testcase started****")
        print("**** Test case ID 002 Verify Bike Routes polyline Testcase started****")

        # Create object for classes
        self.driver = setup
        self.Excel = ReadExcelFile()

        if os == "iOS":
            self.SignIn = iOS_Sign_InPage()
            self.commonMethod = iOS_CommonMethods()
            print("Testcase Run on iOS")
        elif os == "android":
            self.commonMethod = CommonMethods()
            self.SignIn = Sign_InPage()
            print("Testcase Run on android")


        # Reading excelSheet
        Address, Name = self.Excel.readExcelData(self.driver, TestCaseName)

        #Call verify onboarding pages
        self.commonMethod.OnboardingPages(self.driver)

      #Click on sign in Guest button
        if os == "android":
          self.SignIn.SignIn_Guest_Btn(self.driver)

        self.SignIn.WhereTo_Btn(self.driver)
        self.SignIn.TextSearchTab(self.driver, Address)
        self.SignIn.Route_Btn(self.driver)

        self.commonMethod.tear_down(self.driver)

