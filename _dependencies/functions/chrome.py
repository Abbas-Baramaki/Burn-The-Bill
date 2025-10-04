from selenium.webdriver.common.by import By
from ..functions.public import getIp
from ..functions.public import sleep
from ..functions.logging import log
from .App.app import toggle_mobile_data
from selenium import webdriver
from .public import scrolling
import re
sponsered = ["Спонзорисано","Sponsored"]

def fillLinks(driver,Link,Links,scraper):
    try:
        _a = driver.find_elements(By.TAG_NAME,"a")
    except:
        driver.quit()
        scraper()
    for _container in _a:
        _href = _container.get_attribute("href")
        if(_href):
            for _span in _container.find_elements(By.TAG_NAME,"span"):
                if _span.text.strip() in sponsered:
                    _link = Link(_container,_container.id,_href)
                    Links.add_link(_link)
    return Links

def getNewIp(driver,address):
    toggle_mobile_data()
    sleep(32)
# def check(driver,scraper,address=None):
#     try:
        
#         form = driver.find_element(By.ID,"captcha-form")
#         _interrut = driver.text
        
#         if (form.get_attribute("id").strip() == "captcha-form"):
#             log("مرورگر توسط گوگل ربات تشخیص داده شد")
#             driver.execute_script("alert('ربات نیاز به ایپی جدید دارد');")
#             getNewIp(driver,address)
#             driver.quit()
#             scraper()
#         elif 
#     except:
#         log("با موفقیت وارد صفحه اصلی شدیم")
        
def authHandle(driver: webdriver.Chrome, setting, _address="[ No Address ]"):
    try:
        _body = driver.find_element(By.TAG_NAME, "body")

        if True:
            scrolling(driver)

            _errors = 0
            for _error in setting.errors:
                if re.search(_error, _body.text) is None:
                    pass
                else:
                    _errors += 18
                    log(f"{_address} در این آدرس تشخیص داده شدیم")
                    break

            if True:
                sleep(3)
                scrolling(driver)
                sleep(3)
                scrolling(driver)
                sleep(3)
                scrolling(driver)
                log(f"{_address} بازدید با موفقیت ثبت شد ")
    except:
        pass
