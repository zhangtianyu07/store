from selenium import webdriver
import time

#创建
driver = webdriver.Chrome()

#获取网址
driver.get(r"https://www.jd.com")

#窗口最大化
driver.maximize_window()

#登录
driver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()
time.sleep(10)

#购买商品
driver.find_element_by_xpath("//*[@id='key']").send_keys("小米")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()

#切换页面
wins = driver.window_handles
driver.switch_to.window(wins[1])
time.sleep(5)

driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[1]/a/i").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='choose-attr-2']/div[2]/div[3]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(2)

driver.quit()













#获取搜索栏