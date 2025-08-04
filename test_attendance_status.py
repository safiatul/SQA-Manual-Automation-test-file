from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

def test_attendance_reflects_leave():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android Device',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.example.leaveapp',
        'appActivity': 'com.example.leaveapp.MainActivity',
        'noReset': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(3)

    # Navigate to attendance screen
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "AttendanceTab").click()

    # From date
    driver.find_element(AppiumBy.ID, "from_date_input").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("12")').click()
    driver.find_element(AppiumBy.ID, "ok_button").click()

    # To date
    driver.find_element(AppiumBy.ID, "to_date_input").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")').click()
    driver.find_element(AppiumBy.ID, "ok_button").click()

    # Select status
    driver.find_element(AppiumBy.ID, "status_dropdown").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("On Leave")').click()

    time.sleep(2)

    # Validate attendance status
    statuses = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert any("On Leave" in s.text for s in statuses), "On Leave status not shown in attendance list."

    driver.quit()