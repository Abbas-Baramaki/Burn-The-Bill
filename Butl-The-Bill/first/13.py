import time
import random
import pyautogui
import psutil

# from seleniumwire import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

KEYWORD = "امداد خودرو ایران یدک کش بر اصفهان"
MY_SITES = [
    "emdadkhodro110.com",
    "esfahan-emdad.com",
    "mdotcar.com",
    "emdaadkhodrokashan.com",
    "mr-acharfrance.com",
    "emdadkhdrogem.com",
    "emdadzenderod.com",
    "itoll.com",
    "emdadkhodroisf.site"
]

ACCEPT_TEXTS = [
    "I agree", "Accept all", "Agree", "Accept",
    "می‌پذیرم", "تأیید", "قبول", "قبول کردن", "موافقم",
    "J’accepte", "Accepter", "Tout accepter",
    "Aceptar", "Estoy de acuerdo", "Aceptar todo",
    "Akzeptieren", "Alle akzeptieren", "Ich stimme zu",
    "Accetta", "Accetto",
    "Aceitar", "Aceitar tudo", "Concordo",
    "Принять", "Я согласен", "Согласен",
    "同意", "接受", "全部接受",
    "同意する", "すべて同意",
    "동의", "모두 수락",
    "Kabul et", "Tümünü kabul et",
    "أوافق", "قبول", "أوافق على الكل",
    "स्वीकार करें", "सभी स्वीकार करें",
    "Terima", "Setuju", "Terima semua"
]

def accept_google_terms(driver):
    time.sleep(2)
    try:
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            text = btn.text.strip()
            if text in ACCEPT_TEXTS:
                btn.click()
                print(f"✅ پیام گوگل با متن '{text}' پذیرفته شد")
                time.sleep(1)
                return
        print("ℹ️ هیچ دکمه پذیرشی پیدا نشد یا قبلاً بسته شده")
    except Exception as e:
        print(f"⚠️ خطا در پذیرش پیام گوگل: {e}")

def activate_mobile_mode():
    """بعد از سرچ → کلیک راست → Inspect → Mobile Toggle → رفرش"""
    try:
        time.sleep(2)
        pyautogui.rightClick(x=500, y=500)
        time.sleep(2)

        inspect_location = pyautogui.locateCenterOnScreen("inspect_option.png", confidence=0.8)
        if inspect_location:
            pyautogui.click(inspect_location)
            print("✅ Inspect باز شد")
            time.sleep(3)  # صبر برای باز شدن کامل DevTools

            # تلاش چندباره برای پیدا کردن Mobile Toggle
            mobile_toggle = None
            for _ in range(5):
                mobile_toggle = pyautogui.locateCenterOnScreen("mobile_toggle.png", confidence=0.8)
                if mobile_toggle:
                    break
                time.sleep(1)

            if mobile_toggle:
                pyautogui.click(mobile_toggle)
                print("📱 حالت موبایل فعال شد")
                time.sleep(2)
                pyautogui.hotkey("ctrl", "r")  # رفرش صفحه
                print("🔄 صفحه رفرش شد در حالت موبایل")
                time.sleep(4)
            else:
                print("⚠️ آیکن Mobile Toggle بعد از چند تلاش پیدا نشد")
        else:
            print("⚠️ Inspect پیدا نشد")
    except Exception as e:
        print(f"⚠️ خطا در فعال‌سازی حالت موبایل: {e}")

def kill_chrome_processes():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if proc.info['name'] and "chrome" in proc.info['name'].lower():
                proc.kill()
                print(f"💀 پردازش کروم بسته شد: PID {proc.info['pid']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def run_bot():
    options = uc.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # wire_options = {
    #         'proxy': {
    #             'http': 'http://td-customer-KJR0TCDbWoAT1D-continent-as-country-in,ph,sa,vn-sessid-vn9ndtnzm4sbkf356-sesstime-1:wi41Sc8lz@tihb7yjb.as.thordata.net:5555',
    #             'https': 'https://td-customer-KJR0TCDbWoAT1D-continent-as-country-in,ph,sa,vn-sessid-vn9ndtnzm4sbkf356-sesstime-1:wi41Sc8lz@tihb7yjb.as.thordata.net:5555',
    #             'no_proxy': 'localhost,127.0.0.1'  
    #     }
    # }

    driver = uc.Chrome(options=options)

    try:
        driver.get("https://www.google.com")
        
        time.sleep(2)

        accept_google_terms(driver)

        search_box = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_box.clear()
        search_box.send_keys(KEYWORD)
        time.sleep(0.5)
        search_box.send_keys(Keys.RETURN)

        time.sleep(4)

        # ✅ بعد از اومدن نتایج → برو به حالت موبایل
        activate_mobile_mode()

        max_attempts = random.randint(3, 6)
        site_found = False

        for attempt in range(max_attempts):
            ads = driver.find_elements(By.TAG_NAME, "a")
            for ad in ads:
                href = ad.get_attribute("href")
                if href:
                    for site in MY_SITES:
                        if site in href:
                            print(f"✅ سایت پیدا شد: {href} (تلاش {attempt+1})")
                            ad.click()
                            site_found = True
                            time.sleep(random.uniform(2, 3))
                            break
                if site_found:
                    break
            if site_found:
                break

            print(f"🔄 سایت پیدا نشد، رفرش شماره {attempt+1}")
            driver.refresh()
            time.sleep(random.uniform(2, 3))

        if not site_found:
            print(f"❌ بعد از {max_attempts} بار رفرش سایت پیدا نشد، مرورگر بسته می‌شود")
            return

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        time.sleep(1.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)

    finally:
        driver.quit()
        kill_chrome_processes()
        print("♻️ مرورگر کاملاً بسته شد، چرخه بعدی شروع می‌شود")

# اجرای بی‌نهایت
while True:
    try:
        run_bot()
        time.sleep(random.uniform(3, 6))
    except Exception as e:
        print(f"⚠️ خطا رخ داد: {e}")
        time.sleep(random.uniform(5, 10))
