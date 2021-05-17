#1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
# 2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
# 3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
# 4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
# 5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；

#厨师类
class Cook:
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def Zrice(self):
        print("蒸饭！！！")

#厨师子类
class Cookson(Cook):

    def Crice(self):
        print("炒饭！！！")

#厨师子类的子类
class Cooksonson(Cookson):

    def Zrice(self):
        print("蒸饭！！！")

    def Crice(self):
        print("炒饭！！！")

#测试类
class Test:
    cook = Cook()
    cook.setName("张三")
    cook.setAge("20")
    print(cook.getName())
    print(cook.getAge())


sun = Cooksonson()
sun.Zrice()
sun.Crice()















