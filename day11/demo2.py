#有笔记本电脑
# （屏幕大小，价格，cpu型号，内存大小，待机时长）
# 行为（打字，打游戏，看视频）

class computer:
    __screen = ""
    __price = 0
    __cpu = ""
    __time = 0

    def setscreen(self,screen):
        self.__screen = screen

    def getscreen(self):
        return self.__screen

    def setprice(self,price):
        if price <= 0:
            print("你能用这些钱买电脑？呆呆")
        else:
            self.__price = price

    def getprice(self):
        return self.__price

    def setcpu(self,cpu):
        self.__cpu = cpu

    def getcpu(self):
        return self.__cpu

    def settime(self,time):
        if time <= 0:
            print("你用电脑时间这样？呆呆")
        else:
            self.__time = int(time)

    def gettime(self):
        return self.__time

    #方法
    def writer(self):
        print("打字我推荐电脑屏幕大小为：",self.__screen,"的笔记本电脑因为很爽！！！")

    def game(self):
        print("打游戏我推荐电脑cpu最少为：",self.__cpu,"的笔记本电脑，配置越高操作越流畅！！！")

    def video(self):
        print("看视频我推荐电脑价格为",self.__price,"的笔记本电脑，计得每次用电脑待机时长最好在",self.__time,"个小时以内！！！")



c = computer()

c.setscreen("17.3寸")
c.setprice(8900)
c.setcpu("99核处理器cpu")
c.settime(5)

c.writer()
c.game()
c.video()

















