# coding=gbk
#商品
shop = [
    ["黑鹰战机",1500], #0
    ["天启坦克",3000], #1
    ["核潜艇",2000],
    ["乌贼战舰",1000],
    ["自爆卡车",1500],
    ["雇佣兵",200],
    ["猎犬",100],
    ["采矿车",1300],
    ["恐怖机器人",500],
    ["尤里",800],     #9
]

#资金
money = input("请输入您的资金：")
money = int(money)

#购物车
shopcar = []

while True:
    for index,value in enumerate(shop):
        print(index,"    ",value)

    #请输入购买的商品编号
    num = input("请输入要购买的商品编号：")

    if num.isdigit():
        num = int(num)
        if 0 <= num < len(shop):
            if money >= shop[num][1]:
                money = money - shop[num][1]
                shopcar.append(shop[num])
                print("购买成功！！！")
                print("您的当前余额为：",money)
            else:
                print("对不起，您的资金不足！！！")
        else:
            print("该商品不存在！！！请重新输入")

    #输入qQ退出
    elif num == "Q" or num == "q":
        print("退出商城！！！")
        break
    else:
        print("输入非法！！！！\n请重新输入")

#都卖完了需要输出一下购物清单
print("---------购物小票详情----------")
for index,value in enumerate(shopcar):
    print(index,"    ",value)
print("您的当前余额为：",money)
print("【欢迎下次光临！！！】")
























