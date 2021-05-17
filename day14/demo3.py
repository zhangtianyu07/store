#i.	人：年龄，性别，姓名。

class Ren:
    __name = None
    __sex = None
    __age = None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex


# ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。

class Gongren(Ren):

    def Ganhuo(self):
        print("干活！！！")

# iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

class Student(Gongren):

    __num = None

    def setName(self,num):
        self.__num = num
    def getName(self):
        return self.__num

    def Learn(self):
        print("学习！！！")

    def Sing(self):
        print("唱歌！！！")