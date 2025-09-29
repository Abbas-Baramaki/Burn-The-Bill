import random
import time
import selenium
def randomtime(speed)->float:
    return random.uniform(0,1) * speed
def sleep(speed=6):
    time.sleep(randomtime(speed=speed))
    
def typing(element,text):
    for char in text:
        element.send_keys(char)
        sleep(0.45)
def scroll(driver, element , x=0, y=0):
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)

def scrolling(driver):
    total_scroll = random.randint(-300,300)
    step = 10
    for y in range(0, total_scroll, step):
        time.sleep(random.uniform(0.01, 0.1))
        driver.execute_script(f"window.scrollTo(0,{y})")
        
