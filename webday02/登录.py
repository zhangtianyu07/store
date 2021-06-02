from selenium import webdriver
import time

dirver = webdriver.Chrome()
dirver.get("http://8.129.91.152:8765/Index/reg.html")
dirver.maximize_window()
time.sleep(5)
dirver.find_element_by_xpath("//*[@id='phone']").send_keys("13171910307")
time.sleep(30)
dirver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("717tianyu")
time.sleep(5)
dirver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
time.sleep(5)
dirver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
time.sleep(5)

dirver.quit()


