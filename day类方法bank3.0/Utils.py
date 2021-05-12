#随机数类，输入帮助类
import random
class Utils:
    #输入类
    def inputHelp(self,chose,datatype = "str"):
        while True:
            print("请输入" + chose + ":")
            i = input(">>>")
            #strip删除其他输入的格式
            if len(i.strip()) == 0:
                print("该项不能为空，请重新输入！")
                continue
            if datatype != "str":
                return int(i)
            else:
                return i

    #随机数类
    def getRandom(self):
        list = [chr(i) for i in range(97, 123)]
        for i in range(65, 91):
            list.append(chr(i))
        for i in range(10):
            list.append(str(i))
        string = ""
        for i in range(8):
            string += list[int(random.random() * len(list))]
        return string