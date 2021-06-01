from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#创建
driver = webdriver.Chrome()

#获取网址
driver.get(r"https://www.qcc.com")

#窗口最大化
driver.maximize_window()

#延迟
time.sleep(6)

#准备阶段
driver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]/img[1]").click()

#延迟
time.sleep(3)

#登录
driver.find_element_by_link_text("登录 | 注册").click()

#延迟
time.sleep(6)

#获取滑块
ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")

#拉一拉
ac = ActionChains(driver)
ac.click_and_hold(ele).move_by_offset(348,0).perform()

#延迟
time.sleep(3)

#退出
driver.quit()

















