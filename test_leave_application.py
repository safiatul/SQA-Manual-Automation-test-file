from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

def test_apply_leave():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android Device',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.example.leaveapp',  # Replace with your app's package
        'appActivity': 'com.example.leaveapp.MainActivity',  # Replace with your app's activity
        'noReset': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(3)

    # Click on '+' button to apply leave
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "AddButton").click()

    # Select apply date
    driver.find_element(AppiumBy.ID, "apply_date_input").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()
    driver.find_element(AppiumBy.ID, "ok_button").click()

    # Select leave type
    driver.find_element(AppiumBy.ID, "leave_type_dropdown").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Annual Leave")').click()

    # Click submit
    driver.find_element(AppiumBy.ID, "submit_button").click()

    time.sleep(2)

    # Validate leave appears in list
    leaves = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    found = any("Annual Leave" in leave.text for leave in leaves)
    assert found, "Leave not listed after submission."

    driver.quit()