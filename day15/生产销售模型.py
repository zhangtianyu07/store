#生产、销售模型
'''
开发情景：
面包店
6个厨子，5个客户，面包篮子只能存300个
厨师如果发现满了就停三秒，然后继续放
跑5分钟时间
统计厨师总共造了多少个面包
客户买了多少个面包（10/1）
每个客户付了多少钱
'''

import threading
import time

#篮子
lan = 0
#时间类
sj = 0
class Timerun(threading.Thread):
    def run(self) -> None:
        global sj
        while True:
            if sj < 10:
                time.sleep(1)
                sj = sj + 1
            else:
                break

#厨师类
num1 = 0
class Cook(threading.Thread):
    cook = ""
    def run(self) -> None:
        global lan
        global num1
        while sj < 10:
            while lan < 300:
                lan = lan + 1
                num1 = num1 + 1
                print(self.cook,"厨师造了",num1,"个面包！")
            while lan == 300:
                print("暂时不能生产！")
                time.sleep(3)



#客户类
num2 = 0
class Customer(threading.Thread):
    customer = ""
    def run(self) -> None:
        global lan
        global num2
        while sj < 10:
            while lan > 0:
                lan = lan - 1
                num2 = num2 + 1
                print(self.customer,"买了",num2,"个面包,花了",num2 * 10,"元！")



t = Timerun()

c1 = Cook()
c1.cook = "小五"
c2 = Cook()
c2.cook = "小六"
c3 = Cook()
c3.cook = "小七"
c4 = Cook()
c4.cook = "小八"
c5 = Cook()
c5.cook = "小久"
c6 = Cook()
c6.cook = "小十"

r1 = Customer()
r1.customer = "一号"
r2 = Customer()
r2.customer = "二号"
r3 = Customer()
r3.customer = "三号"
r4 = Customer()
r4.customer = "四号"
r5 = Customer()
r5.customer = "五号"

t.start()
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()

r1.start()
r2.start()
r3.start()
r4.start()
r5.start()



