#账号和密码
name = "root"
password = "admin"
count = 1
num3 = 2
while True:
    num1 = input("账号：")
    num2 = input("密码：")
    if count < 3:
        count = count +1
        if num1 == name and num2 == password:
            print("账号密码正确！！！")
            break
        else:
            print("对不起，输入密码有误！")
    else:
        print("三次密码输入错误账号密码锁定！！！！")
        break




