from appium import webdriver
import time

#Appium Server端口默认为4723
server = r'http://localhost:4723/wd/hub'
desired_capabilities = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:62001',
    'platformVersion':'7.1.2',
    'appPackage':'com.jingdong.app.mall',
    'appActivity':'com.jingdong.app.mall.main.MainActivity'
}
driver = webdriver.Remote(server,desired_capabilities)
driver.find_element_by_id("com.jingdong.app.mall:id/bqd").click()
time.sleep(10)
driver.tap([(844,98)],50)
time.sleep(2)
driver.find_element_by_class_name("android.widget.ViewFlipper").click()
time.sleep(4)
driver.find_element_by_id("com.jd.lib.search.feature:id/zw").send_keys("小米11")
time.sleep(3)
driver.find_element_by_id("com.jingdong.app.mall:id/a9b").click()
time.sleep(3)
driver.find_element_by_xpath("(//android.widget.TextView[@content-desc='小米（MI）11'])[1]").click()
time.sleep(3)
driver.find_element_by_id("com.jd.lib.productdetail.feature:id/add_2_car").click()
time.sleep(3)
driver.tap([(448,1537)],50)
time.sleep(3)
driver.tap([(680,1550)],50)
time.sleep(3)
driver.tap([(770,1544)],50)
time.sleep(3)
driver.tap([(682,418)],50)
time.sleep(3)
driver.tap([(86,353)],50)
time.sleep(3)
driver.tap([(165,576)],50)
time.sleep(3)
driver.tap([(68,708)],50)
time.sleep(3)


driver.quit()