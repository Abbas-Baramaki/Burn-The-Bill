import time
import datetime
import random
import re

from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import undetected_chromedriver as uc
import ua_generator



#// mine

from _classes.setting import Setting
from _classes._link import Links
from _classes.Link import Link
from _classes._handles import Handles
from _classes.Address import Address
from _dependencies.functions.logging import log
from _dependencies.functions.public import randomtime , sleep , scroll , typing , scrolling , getIp , likelihood 
from _dependencies.functions.chrome import fillLinks , getNewIp, authHandle
from _dependencies.functions.App.app import Mobile
#// mine

setting = Setting()
setting.fill()
address = Address("192.168.1.1")
# address = Address(getIp())
Links = Links()
mobile_emulation = {
    "deviceName": "Pixel 2" 
}
mobile = Mobile()
chrome_options = uc.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

chrome_options.add_argument("--incognito")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(f"--user-agent={ua_generator.generate(device='mobile',platform='ios',browser='chrome')}")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
if setting.proxy_server:
    wire_options = {
            'proxy': {
                'http': 'http://td-customer-IfAQNf534fkj:mUwxx5wls9vd@tihb7yjb.pr.thordata.net:9999',
                'https': 'https://td-customer-IfAQNf534fkj:mUwxx5wls9vd@tihb7yjb.pr.thordata.net:9999',
                'no_proxy': 'localhost,127.0.0.1'  
        }
    }
else :
        wire_options = {
    }

def scraper():
    global chrome
    mobile = Mobile()
    mobile.init()
    chrome = webdriver.Chrome(options=chrome_options,seleniumwire_options=wire_options)
    setting = Setting()
    setting.fill()
    chrome.get(f"https://google.com/")
    log("مرورگر وارد گوگل شد")
    scrolling(chrome)
    
    _buttons = WebDriverWait(chrome,15).until(EC.presence_of_all_elements_located((By.TAG_NAME,"button")))
    try :
        for _button in _buttons:
            try:
                _div = _button.find_element(By.TAG_NAME,"div")
                if _div.text.strip() in setting.accepts:
                    sleep()
                    scroll(chrome,_div,0,400)
                    sleep(9)
                    _div.click()
                    _button.click()
                    
                    log("پاپ اپ هندل شد")
                    break
            except Exception as ex:
                pass
        del _button
    except:
        log("پاپ اپی برای استارت تعریف نشده")

    _searchElement = WebDriverWait(chrome,15).until(EC.visibility_of_element_located((By.NAME,"q")))
    sleep(12)
    scrolling(chrome)
    typing(_searchElement,setting.query)
    sleep(12) 
    _searchElement.send_keys(Keys.ENTER)
    
    del _searchElement       
    
    authHandle(chrome,setting)
    
    try:
        
        form = chrome.find_element(By.ID,"captcha-form")
        
        if (form.get_attribute("id").strip() == "captcha-form"):
            log("مرورگر توسط گوگل ربات تشخیص داده شد")
            chrome.execute_script("alert('ربات نیاز به ایپی جدید دارد');")
            getNewIp(mobile)
            chrome.close()
            scraper()
    except:
        log("با موفقیت وارد صفحه اصلی شدیم")
    try :
        _buttons = WebDriverWait(chrome,15).until(EC.presence_of_all_elements_located((By.TAG_NAME,"button")))
        if _buttons is not None:
            for _button in _buttons:
                try:
                    _div = _button.find_element(By.TAG_NAME,"div")
                    if _div.text.strip() in setting.accepts:
                        sleep()
                        scroll(chrome,_div,0,400)
                        sleep(7)
                        _div.click()
                        log("در صفحه اصلی پاپ اپی پیدا نشد ")
                        
                        break
                except:
                    pass
    except:
        log("در صفحه اصلی پاپ اپی پیدا نشد ")


    # for _container in _a:
    #     _href = _container.get_attribute("href")
    #     if(_href):
    #         for _span in _container.find_elements(By.TAG_NAME,"span"):
    #             if _span.text.strip() == "Sponsored":
    #                 _link = Link(_container,_container.id,_href)
    #                 Links.add_link(_link)
    out = fillLinks(chrome,Link,Links,scraper)
    try:
        
        if len(out.links) != 0:
            for i in range(len(out.links)):
                _link = Links.links[i]

                if likelihood(setting,_link.address):
                    
                    # _link.view(chrome)
                    _link.container.click()
                    _address = _link.address
                    authHandle(chrome,setting,_address)
                    sleep(3)
                    getNewIp(mobile)
                    sleep(3)
                else :
                    log(f"{_link.address} جزو تارگت های ما نیست")
            log("تمامی اسپانسر ها با موفقیت چک شدند")
            getNewIp(mobile)
            chrome.close()
            log("مرورگر برای بازکردن مجدد تبلیغ ها بسته شد")
            scraper()
            
            
        else:
            log("اسپانسر پیدا نشد مرورگر بسته شد")
            getNewIp(mobile)
            chrome.close()
            scraper()
            

        # scraper()
    except Exception as ex:
        log(f"مشکل ناشناخته ای رخ داده {ex}")
        getNewIp(mobile)
        chrome.close()
        scraper()
        
        
        


            
        


# _submits = chrome.find_elements(By.TAG_NAME,"button")
# for _submit in _submits :
#     if _submit.get_attribute("jsaction") == "click:.CLIENT":
#         _submit.click()
#         print("Clicked")



if __name__ == "__main__":
    log("برنامه استارت شد ----")
    while True:
        try:
            scraper()
            sleep()
            chrome.close()
        except Exception as ex:
            log(f"[1304] خطا هنگام اجرای برنامه \n{ex}\n")
            chrome.close()