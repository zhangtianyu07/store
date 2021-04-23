#随机点名游戏
import random
#先创造列表
num = ["大毛","二毛","三毛","四毛","五毛","小明"]

#设置无限死循环true
while True:
    print("1.随机点名\t2.随机处罚\tq/Q退出")
    #设置一个输入的值
    a = input("请输入编号：")
    #判断输入是否为数字1，2，还是q/Q，或者其他
    if a.isdigit():
        a = int(a)
        if a == 1:
            num1 = random.randint(0,len(num))
            print(num[num1])
        elif a == 2:
            b = random.randint(0,100)
            print(num[num1],"犯错被处罚了",b,"遍！")
    elif a == "q" or a == "Q":
        print("退出程序")
        break
    else:
        print("输入非法，请重新输入！！！")
