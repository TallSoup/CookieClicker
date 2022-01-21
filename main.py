from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# create Selenium driver object
s = Service("C:/Users/andre/Desktop/DevTools/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# target website, max window (not running headless, this is fun to watch)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

# let all parts of website load up, accept cookies (pun intended?)
time.sleep(5)
accept_cookies = driver.find_element(By.CSS_SELECTOR, ".cc_btn")
accept_cookies.click()

# the big cookie to be clicked
cookie = driver.find_element(By.ID, "bigCookie")

# variables to used in gradually increasing upgrade times
count = 0
clicks = 0
interval = 500

while True:
    try:
        cookie.click()
        count += 1
        clicks += 1
        # cookie_count = driver.find_element(By.ID, "cookies")
        # cookie_count = cookie_count.text.split()[0].replace(",", "")

        # upgrades section
        if count % interval == 0:
            # find most expensive item in store and buy it
            equipment = driver.find_elements(By.CSS_SELECTOR, ".enabled")
            equipment[-1].click()

            # reset count to begin counting up to the new interval
            count = 0

            # increase interval by 10%, this ensures we save to buy more expensive items (important in mod-late game)
            interval = round(interval * 1.1, 0)

            # log each upgrade
            print(f"interval={interval}, clicks={clicks}")
            print(equipment[-1].text)

    # occasionally there are popups that get in the way of an upgrade (typically a super cookie)
    # this will ignore and keep code running
    # improvement would be to click the super cookie when it appears
    except Exception as e:
        print(e)
