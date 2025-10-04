from appium import webdriver
from appium.options.android import UiAutomator2Options
import time


def toggle_mobile_data():
    caps = {
        "platformName": "Android",
        "deviceName": "2429c3a4",
        "automationName": "UiAutomator2",
        "noReset": True
    }

    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    try:
        driver.open_notifications()
        driver.tap([(366, 467)])
        time.sleep(2)
        driver.tap([(366, 467)])
        time.sleep(4)
        driver.tap([(530, 530)])
    except Exception as ex:
        print("Error:", ex)
    finally:
        driver.quit()

