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

from _dependencies.functions.logging import log
from _dependencies.functions.public import randomtime , sleep , scroll , typing , scrolling
from _dependencies.functions.chrome import fillLinks
#// mine

setting = Setting()
setting.fill()

Links = Links()
state = -random.randint(-100000000,0)

mobile_emulation = {
    "deviceName": "Pixel 2" 
}

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
    setting = Setting()
    setting.fill()
    chrome = webdriver.Chrome(options=chrome_options,seleniumwire_options=wire_options)
    sponser_attemps = 0

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
                    sleep(7)
                    sleep()
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
    
    try:
        
        form = chrome.find_element(By.ID,"captcha-form")
        if (form.get_attribute("id").strip() == "captcha-form"):
            
            log("مرورگر توسط گوگل ربات تشخیص داده شد")
            chrome.quit()
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
                if _link in setting.my_sites:
                    _link.container.click()
                    _address = _link.address

                    sleep(10)
                    try:
                        _body = chrome.find_element(By.TAG_NAME,"body")
                    
                        if True:
                            scrolling(chrome)

                            _errors = 0
                            for _error in setting.errors:
                                if re.search(_error, _body.text) is None:
                                    pass
                                else:
                                    _errors += 1
                                    log(f"{_address} در این آدرس تشخیص داده شدیم")
                                    break
                                    
                            if True:
                                _link.view()
                                sleep(3)
                                scrolling(chrome)
                                sleep(3)
                                scrolling(chrome)
                                sleep(3)
                                scrolling(chrome)
                                log(f"{_address} بازدید با موفقیت ثبت شد ") 
                    except:
                        pass

                    sleep(4)

                    chrome.back()
                    out = fillLinks(chrome,Link,Links,scraper)
                    setting.my_sites.append(_address)
                    
                    sleep(8)
            log("تمامی اسپانسر ها با موفقیت چک شدند")
            chrome.quit()
            log("مرورگر برای بازکردن مجدد تبلیغ ها بسته شد")
            scraper()
        else:
            log("اسپانسر پیدا نشد مرورگر بسته شد")
            chrome.quit()
            scraper()

        # scraper()
    except Exception as ex:
        log(f"مشکل ناشناخته ای رخ داده {ex}")
        chrome.quit()
        scraper()
        


            
        


# _submits = chrome.find_elements(By.TAG_NAME,"button")
# for _submit in _submits :
#     if _submit.get_attribute("jsaction") == "click:.CLIENT":
#         _submit.click()
#         print("Clicked")



if __name__ == "__main__":
    log("برنامه استارت شد ----")
    scraper()