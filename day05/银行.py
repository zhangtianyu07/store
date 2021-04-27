# 1.	编程实现：仔细业务之间的包含关系，并完成以下编程需求，要适当提高代码的可复用性。
# a)	用户：账号（str：系统随机产生8位数字）、姓名(str)、密码(int:6位数字)、地址、存款余额(int)、开户行（银行的名称（str））
# b)	地址：国家(str)、省份(str)、街道(str)、门牌号(str)
# c)	银行：能存储100用户的库(可用字典，可用列表)、本银行名称（比如：中国工商银行的昌平支行,str）
import random
ID = random.randint(10000000,100000000)
count = 0
list = []


print("***************************************")
print("*             中国工商银行              *")
print("*             账户管理系统              *")
print("***************************************")
print("")
print("* 1 . 开户                            *")
print("* 2 . 存钱                            *")
print("* 3 . 取钱                            *")
print("* 4 . 转账                            *")
print("* 5 . 查询                            *")
print("* 6 . Byb！                           *")
print("***************************************")
while True:

    print("您的账号为：",ID)
    list.append(ID)
    name = input("请输入您的姓名：")
    list.append(name)
    #密码
    while count < 4:
        password = input("密码：")
        if len(password) < 6:
            print("输入错误！！！密码小于6位数")
            print("请重新输入")
            count = count + 1
            if count == 4:
                print("三次密码输入未成功！！！退出系统")
                break
        elif len(password) > 6:
            print("输入错误！！！密码大于6位数")
            print("请重新输入")
            count = count + 1
            if count == 4:
                print("三次密码输入未成功！！！退出系统")
                break
        else:
            password = int(password)
            count = count + 4
            list.append(password)
    count = 0
    address = input("请输入您的地址：")
    list.append(address)
    balance = int(input("请输入您的余额："))
    list.append(balance)
    bank = input("请输入您的开户行：")
    list.append(bank)
    country = input("请输入您的国家：")
    list.append(country)
    province = input("请输入您的省份：")
    list.append(province)
    way = input("请输入您的街道：")
    list.append(way)
    roomnumber = input("请输入您的门牌号：")
    list.append(roomnumber)
    print(list)