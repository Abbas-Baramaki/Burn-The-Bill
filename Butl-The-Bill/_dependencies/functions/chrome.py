from selenium.webdriver.common.by import By

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