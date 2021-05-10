'''
    面向对象

'''
class car:
    #车的属性
    carsum = 0
    carcolor = ""
    carchair = ""
    cartype = ""
    carweight = 0

    #车的行为（方法）
    def carmethod(self):
        print("一辆",self.cartype,"它拥有",self.carsum,"个轮胎,车身是漂亮的",self.carcolor,"可以承载",self.carchair,"个人","车重",self.carweight,"kg")


c = car()
#定义车的属性值
c.carsum = 4
c.carcolor = "小骚粉"
c.carchair = "7"
c.cartype = "五菱神车"
c.carweight = 1000
#调用车的方法执行
c.carmethod()



#一个人
class ren:
    yanjing = ""
    bizi = ""
    zuiba = ""
    erduo = ""
    naodai = ""

    def smile(self):
        print("一个人",self.naodai,"上面长有",self.yanjing,self.bizi,self.zuiba,self.erduo,"，虽然长得正常但是傻的一皮！！！")


r = ren()
r.yanjing = "眼睛"
r.zuiba = "嘴巴"
r.bizi = "鼻子"
r.erduo = "耳朵"
r.naodai = "脑袋"

r.smile()








