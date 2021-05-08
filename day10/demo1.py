#以下文件是用户的一些数据（姓名、年龄、净资产）
# ，要求使用数据库工具将文件中的数据写入到数据库中。
# 并统计所有人的资产总和！

#调用数据库工具包
from DBUtile import update
from DBUtile import select

# #数据变量
# name = input("请输入您的名字：")
# age = input("请输入您的年龄：")
# money = input("请输入您的净资产：")
users = []

f = open(file="用户.txt",mode="r+",encoding="utf-8")
data = f.readlines()

for i in data:
    da = i.replace("\n","").split(",")
    users.append(da)
print(users)
while True:
    print("--------------------------")
    print("是否向数据库中存储数据>>>（输入数字 1 开始存储）（输入字母 Q，q 退出存储）")
    num = input("请输入您的操作选项：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            #数据变量
            # name = input("请输入您的名字：")
            # age = input("请输入您的年龄：")
            # money = input("请输入您的净资产：")
            for i in users:
                sql = "insert into ren values(%s,%s,%s)"
                param = [i[0],i[1],i[2]]
                update(sql,param)
            print("存入成功！！！")
        else:
            print("输入非法！请重新操作")
    elif num == "Q" or num == "q":
        print("退出存储数据库！！！")
        break
    else:
        print("输入非法！请重新操作")
    #向数据库中存储数据
#统计所有人资产总和
while True:
    print("是否需要统计所有人的资产总和！>>>（T t 是）（F f 否）")
    num1 = input("请输入您的选择")
    if num1 == "T" or num1 == "t":
        sql1 = "select sum(money) from ren"
        date1 = select(sql1,[])
        sum = date1[0][0]
        print("所有人的资产总和为：",sum)
        break
    elif num1 == "F" or num1 == "f":
        print("退出！！！")
        break
    else:
        print("输入非法！！！重新选择")




