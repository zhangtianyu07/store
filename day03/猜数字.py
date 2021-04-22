import random

#随机出数
num = random.randint(0,101)

#次数
count = 0
#金币
money = 0
#while循环
#True死循环
while True:
    num1 = int(input("请输入您要猜的数字："))
    count = count + 1
    money = money + 10
    if count < 7:
        if num1 > num:
            print("大了！")
        elif num1 < num:
            print("小了！")
        else:
            print("恭喜您！猜对了",num,"您一共猜了",count,"次","你花了",money,"块钱")
            break
    else:
        print("七次未输入成功，锁定！！！")
        break