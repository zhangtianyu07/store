#分析一个水杯的属性和功能，使用类描述并创建对象
#高度，容积，颜色，材质
#能存放液体

class waterb:
    #属性
    __height = 0
    __volume = 0
    __color = ""
    __type = ""

    def setheight(self,height):
        if height <= 0:
            print("瞎输入个der！")
        else:
            self.__height = height

    def getheight(self):
        return self.__height

    def setvolume(self,volume):
        if volume <= 0:
            print("瞎输入个der！!")
        else:
            self.__volume = volume

    def getvolume(self):
        return self.__volume

    def setcolor(self,color):
        self.__color = color

    def getcolor(self):
        return self.__color

    def settype(self,type):
        self.__type = type

    def gettype(self):
        return self.__type

    #方法
    def leavewith(self):
        print("我有一个水杯，高度为",self.__height,
              "容积为",self.__volume,"颜色是"
              ,self.__color,"材质很牛逼是",self.__type,"它能存放液体！")

w = waterb()
w.setheight(500)
w.setvolume(1000)
w.setcolor("小骚粉")
w.settype("钛金属")

w.leavewith()
















