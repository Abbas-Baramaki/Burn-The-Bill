from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from _classes.setting import Setting
from _dependencies.functions.public import sleep
from _dependencies.functions.logging import log

class Mobile:
    def __init__(self):
        self.driver = None
        
    def init(self)->bool:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "60baa866"
        options.automation_name = "UIAutomator2"
        self.driver =  webdriver.Remote("http://127.0.0.1:4723", options=options)
        log("موبایل با موفقیت کانفیگ شد")
        
    def airplane(self,setting:Setting):
        setting = Setting()
        setting.fill()
        try:
            self.driver.open_notifications()
            sleep(7)
            self.driver.tap([(setting.airplane_x,setting.airplane_y)])
            sleep(5)
            self.driver.back()
            self.driver.back()
            

            self.driver.open_notifications()
            sleep(7)
            self.driver.tap([(setting.airplane_x,setting.airplane_y)])
            sleep(5)
            self.driver.back()
            self.driver.back()
        except Exception as ex:
            log(f"موبایل خطا داد \n{ex}\n")
        finally:
            self.driver.quit()
            del self.driver

