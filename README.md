# Mobile Automation Pytest Framework
Appium Hybrid Framework
(Python, pytest, appium, selenium, Page Object Model, HTML report, Allure report)
Prerequisite: 
1. Python should be install
2. Pycharm IDE should be install
3. Appium should be install
4. Android & iOS setup should be install

Step 1: Create new Project & Install required Packages/plugins
Selenium: Selenium Libraries
Pytest: Python UnitTest framework
Pytest-html: PyTest HTML Reports
Pytest-xdist: Run Tests parallel
Openpyxl: MS Excel Support
Allure-pytest: to generate allure report

Step 2: Create Folder Structure
Project Name 
| 
Android_PageObjects (Package)
|
iOS_PageObjects (Package)
|
Configuration
|
Logs
|
Reports
|
TestCases
|
TestData
|
Utilities
|
Venv
    |
    Run.sh
    |
    Requirement.txt


Step 3: Automating Login Testcases
3.1: Create page object class under “Android_PageObjects” & “iOS_PageObjects”.
3.2: Create Test under “TestCases”.
3.3: Create conftest.py under “TestCases”.

Step 4: Capture screenshot on failures
4.1: Update Testcase with screenshot under “TestCases”.

Step 5: Read common values from ini file
5.1: Add “config.ini” file “Configuration” folder.
5.2: Create “readProperties.py” utility file under utilities package to read common data. 

Step 6: Adding logs to test cases
6.1 : Add customLogger.py under utilities package.
6.2: Add logs to login test case.

Step 7: Generate pytest HTML Reports.
7.1: Update conftest.py with pytest hooks.
7.2: To Generate HTML report run below command:
Python3 -v -m pytest --html=Reports/RidePlanReport.html TestCases/ --os android

Step 8: Automating Data Driven Testcases
   8.1: Prepare test data in Excel sheet, place the excdel file inside the TestData folder.
   8.2: Create “ExcelTestCase.py” utility class under utilities package.
   8.3: Read ExcelTestCases.py class in required tetscases for reading data.

Step 9: Grouping Tests
   9.1: Grouping markers(Add markers to every test method)
@pytest.mark.sanity
@pytest.mark.regression

9.2: Add Marker entries in pytest.ini file
pytest.ini
------
[pytest]
Markers = 
   sanity
regression
    9.3: Select groups at run time
        -m “sanity”
        -m “regression”
        -m “sanity and regression”
        -m “sanity or regression”
Run command:
Python3 -v -m pytest “sanity and regression” --html=Reports/RidePlanReport.html TestCases/ --os android

    
Step 10: Run tests in command promt & run.sh file.
     10.1: create run.sh file & write command here then run that file

Step 11: Generate allure report
    
Run below command-

python3 -v -m pytest --alluredir=./Reports/report TestCases/ --os android

allure serve Reports/report

 
