import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    # browser.get('https://www.baidu.com')
    # # selenium 元素查找find_element_by_id方法，找到元素后输入信息
    # input = browser.find_element_by_id('kw')
    # input.send_keys('Python')
    # input.send_keys(Keys.ENTER)
    # # 等待时间 10s
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookies())
    # print(browser.page_source)
    #

    #  DOM选择器
    # browser.get("http://localhost:8088/admin/Login.aspx")
    #
    # usernameInput = browser.find_element_by_id('id_username')
    # passwordInput = browser.find_element_by_id('id_password')
    #
    # usernameInput.send_keys('admin')
    # passwordInput.send_keys('admin')
    # loginBtn = browser.find_element_by_id('btn_login')
    # loginBtn2 = browser.find_element_by_css_selector('#btn_login')
    # loginBtn3 = browser.find_element_by_xpath('//button[@id="btn_login"]')
    # loginBtn4 = browser.find_element(By.ID, 'btn_login')
    #
    # # loginBtn.send_keys(Keys.ENTER)
    # print(usernameInput)
    # print(passwordInput)
    # print(loginBtn)
    # print(loginBtn2)
    # print(loginBtn3)
    # print(loginBtn4)
    #
    # browser.get('https://www.taobao.com')
    # lis = browser.find_elements_by_css_selector('.service-bd li')
    # lis1 = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
    # print(lis)
    # print(lis1)

    #  按钮点击事件
    # input = browser.find_element_by_id('q')
    # input.send_keys('iPhone')
    # time.sleep(1)  # 休眠1s
    # input.clear()  # 清除输入框数据
    # input.send_keys('iPad')
    # button = browser.find_element_by_class_name('btn-search')
    # button.click()  # 获取按钮的点击

    #  执行动作链
    # url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    # browser.get(url)
    # browser.switch_to.frame('iframeResult')
    # source = browser.find_element_by_css_selector('#draggable')
    # target = browser.find_element_by_css_selector('#droppable')
    # actions = ActionChains(browser)  # 声明ActionChains对象并将其赋值为actions变量
    # actions.drag_and_drop(source, target)
    # actions.perform()

    # 执行script
    # browser.get('https://www.zhihu.com/explore')
    # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # browser.execute_script('alert("To Bottom")')
    # browser.switch_to.alert.accept()

    # 获取节点信息
    # url = 'https://www.zhihu.com/explore'
    # browser.get(url)
    # logo = browser.find_element_by_id('special')
    # print(logo)
    # print(logo.get_attribute('class'))
    #
    # button = browser.find_element_by_class_name('Button--blue')
    # print(button.text)
    # print(button.location)
    # print(button.id)
    # print(button.tag_name)
    # print(button.size)

    # 获取子iframe
    # url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    # browser.get(url)
    # # 切换到某个iframe
    # browser.switch_to.frame('iframeResult')
    # try:
    #     logo = browser.find_element_by_class_name('logo')
    # except NoSuchElementException:
    #     print('NO LOGO')
    # # 切换回父节点
    # browser.switch_to.parent_frame()
    # logo = browser.find_element_by_class_name('logo')
    # print(logo)
    # print(logo.text)

    # 显示等待加载
    # browser.get('https://www.taobao.com/')
    # wait = WebDriverWait(browser, 10)
    # # 所有节点加载出来才节点
    # input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
    # button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    # print(input, button)

    # 前进或者后退
    # browser.get('https://www.baidu.com/')
    # browser.get('https://www.taobao.com/')
    # browser.get('https://www.cnblogs.com/weihanli/p/9874971.html')
    # browser.back()
    # time.sleep(1)
    # browser.forward()

    # 获取cookie内容
    # browser.get('https://www.zhihu.com/explore')
    # print(browser.get_cookies())
    # browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    # print(browser.get_cookies()[0])
    # print(browser.get_cookies()[0]['domain'])
    # browser.delete_all_cookies()
    # print(browser.get_cookies())

    # 选项卡管理
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')  # 打开新的选项卡
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])  # 切换选项卡
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to_window(browser.window_handles[0])
    browser.get('https://python.org')
except UnexpectedAlertPresentException:
    # 捕获异常
    print("###UnexpectedAlertPresentException")
finally:
    browser.close()
