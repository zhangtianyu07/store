from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#创建
driver = webdriver.Chrome()

#获取网址
driver.get(r"https://www.suning.com")

#全屏显示
driver.maximize_window()

#延迟
time.sleep(2)

#获取搜索栏
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("AK47")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

#延迟
time.sleep(3)

driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_04:0071003558_11910374045']/img").click()

#延迟
time.sleep(3)
#获取网页个数
wins = driver.window_handles
#切换网页
driver.switch_to.window(wins[1])

driver.find_element_by_xpath("//*[@id='colorItemList']/dd/ul/li[1]/a").click()
#延迟
time.sleep(2)
driver.find_element_by_xpath("//*[@id='buycount']/dd/a[2]").click()
#延迟
time.sleep(2)
driver.find_element_by_xpath("//*[@id='addCart']").click()
#延迟
time.sleep(2)

#退出
driver.quit()





















