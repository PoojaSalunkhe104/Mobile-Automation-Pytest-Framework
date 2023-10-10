from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
     "deviceName": "Emaulator",
      "platformName": "Android",
      # "app": "/Users/macbook/Downloads/app-arevo-staging.apk"
      "app": "/Users/macbook/Documents/app-tfnsw-staging-bitrise-signed.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(10)
input = driver.find_element(MobileBy.XPATH,'//android.widget.TextView[@content-desc="Continue, button"]')
input = input.text
print('input is: '+input)

inputA = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Continue, button"]'))
)
inputA.click()
print('1. Click on continue')

inputB = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Continue, button"]'))
)
inputB.click()
print('2. Click on continue')

inputC = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Continue, button"]'))
)
inputC.click()
print('3. Click on continue')

inputD = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Continue, button"]'))
)
inputD.click()
print('4. Click on continue')

alert_obj = driver.switch_to.alert;
alert_obj.accept();
time.sleep(10);
alert_obj.accept();
print('accept alert');

time.sleep(10);
driver.quit()