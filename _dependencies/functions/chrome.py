from selenium.webdriver.common.by import By
from ..functions.public import getIp
from ..functions.public import sleep
from ..functions.logging import log
from .App.app import toggle_mobile_data
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
    sleep(20)
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
        
        
    
    