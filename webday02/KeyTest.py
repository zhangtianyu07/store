from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#创建
driver = webdriver.Chrome()

#获取网址
driver.get(r"https://www.baidu.com")

#屏幕最大化
driver.maximize_window()

#获取输入框
driver.find_element_by_xpath("//*[@id='kw']").click()
time.sleep(2)

#键盘事件
ac = ActionChains(driver)
ac.key_down("x").key_up("x").perform()
time.sleep(2)

driver.quit()