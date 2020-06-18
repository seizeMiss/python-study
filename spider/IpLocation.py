import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get("https://tool.lu/ip/")

    #  按钮点击事件
    input = browser.find_element_by_name('ip')
    input.clear()
    input.send_keys('113.92.95.212')
    # time.sleep(1)  # 休眠1s
    button = browser.find_element_by_css_selector('#main_form .waves-effect')
    button.click()  # 获取按钮的点击
    time.sleep(2)

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    for x in soup.findAll('td', id="ip2region_address"):
        print(x.text)

except UnexpectedAlertPresentException:
    # 捕获异常
    print("###UnexpectedAlertPresentException")
finally:
    browser.close()
