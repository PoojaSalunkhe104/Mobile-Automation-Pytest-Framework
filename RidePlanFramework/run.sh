#!/bin/bash
#python3 -v -m pytest --html=Reports/RidePlan.html TestCases/test_FirstTestCase.py --os android
#python3 -v -m pytest --alluredir=./Reports/report TestCases/ --os android
#allure serve Reports/report
#python3 -v -m pytest --html=./Reports/auto.html TestCases/test_VerifyOnboardingPages.py --os android
#python3 -v -m pytest --html=Reports/RidePlan.html TestCases/test_VerifyBikeRoutes.py --os android
#python3 -v -m pytest --alluredir=./Reports/report TestCases/test_VerifyOnboardingPages.py --os android
#python3 -v -m pytest --alluredir=./Reports/report TestCases/test_VerifyOnboardingPages.py --os iOS
python3 -v -m pytest --alluredir=./Reports/report TestCases/ --os android

allure serve Reports/report


