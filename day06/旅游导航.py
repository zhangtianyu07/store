#字典使用写位置地址
import random
#城市地点内容设计
city = {
    "北京":{
        "昌平":{
            "回龙观" : ["超市","公司","电影院"],
            "龙泽" : ["超市","公司","电影院"]
        },
        "朝阳" : {
            "三里屯":["超市","公司","电影院"],
            "大悦城":["超市","公司","电影院"]
        },
        "东城" : {
            "东单":["超市","公司","电影院"],
            "芳草地":["超市","公司","电影院"]
        },
        "西城" : {
            "西单":["超市","公司","电影院"],
            "旧时代":["超市","公司","电影院"]
        },
        "海淀" : {
            "清华":["超市","公司","电影院"],
            "北大":["超市","公司","电影院"]
        },
        "丰台" : {
            "动物园":["超市","公司","电影院"],
            "植物园":["超市","公司","电影院"]
        }
    },
    "天津":{
        "南区":{
            "分手之眼":["超市","公司","电影院"],
            "不分手之眼":["超市","公司","电影院"]
        },
        "北区":{
            "武当山":["超市","公司","电影院"],
            "峨眉山":["超市","公司","电影院"]
        }
    }
}

#商城需要的内容
shop = [
    ["黑鹰战机",1500], #0
    ["天启坦克",3000], #1
    ["核潜艇",2000],
    ["乌贼战舰",1000],
    ["自爆卡车",1500],
    ["雇佣兵",200],
    ["猎犬",100],
    ["采矿车",1200],
    ["恐怖机器人",500],
    ["尤里",800],     #9
]
shop1 = [shop[1][0],shop[1][1] / 2]
shop2 = [shop[7][0],shop[7][1] / 600 * 300]



#展示城市
def print_place(city):
    for i in city:
        print(i)

#城市旅游公司
while True:
    print("----------------------欢迎来到旅游导航界面---------------------")
    print_place(city)
    num1 = input("请输入您要去的城市》》》》》")
    if num1 in city:        #北京、天津
        print_place(city[num1])
        num2 = input("请输入您要去的区域》》》》》")
        if num2 in city[num1]:
            print_place(city[num1][num2])
            num3 = input("请输入您要去的地方》》》》》")
            if num3 in city[num1][num2]:
                print_place(city[num1][num2][num3])
                num4 = input("请输入您要去的场所》》》》》")
                if num4 == "超市":
                    print("--------------------欢迎来到军火超市-------------------")
                    money = input("请输入您的资金：")
                    money = int(money)
                    money1 = money
                    #购物车
                    shopcar = []
                    yhq = random.randint(1,31)
                    print(yhq)
                    print("---------优惠券种类---------")
                    print("1~10、 10张采矿车优惠券：满600减300\n11~30、 20张天启坦克优惠券：半折甩卖")
                    print("---------------------------")

                    if 1 <= yhq <= 10:
                        print("恭喜您！抽到1张采矿车优惠券：满600减300")
                        be2 = 0
                        be1 = 1
                    else:
                        print("恭喜您！抽到1张天启坦克优惠券：半折甩卖")
                        be1 = 0
                        be2 = 1

                    while True:
                        for index,value in enumerate(shop):
                            print(index,"    ",value)

                        #请输入购买的商品编号
                        num = input("请输入要购买的商品编号：")

                        if num.isdigit():
                            num = int(num)
                            if 0 <= num < len(shop):
                                #购买天启坦克情况
                                if num == 1:
                                    #有无优惠券判断
                                    if be1 == 0:
                                        print("存在优惠券是否使用》》》【1、是】【2、否】")
                                        kc = int(input(":"))
                                        #是否使用优惠券判断
                                        if kc == 1:
                                            be1 = be1 + 1
                                            if money >= shop[num][1]:
                                                money = money - shop1[1]
                                                shopcar.append(shop1)
                                                print("购买成功！！！")
                                                print("您的当前余额为：",money)
                                            else:
                                                print("对不起，您的资金不足！！！")
                                            # else:
                                            #     print("已使用过优惠券，暂无优惠券！！！")
                                        elif kc == 2:
                                            if money >= shop[num][1]:
                                                money = money - shop[num][1]
                                                shopcar.append(shop[num])
                                                print("购买成功！！！")
                                                print("您的当前余额为：",money)
                                            else:
                                                print("对不起，您的资金不足！！！")

                                        else:
                                            print("输入非法！！！")
                                    else:
                                        if money >= shop[num][1]:
                                            money = money - shop[num][1]
                                            shopcar.append(shop[num])
                                            print("购买成功！！！")
                                            print("您的当前余额为：",money)
                                        else:
                                            print("对不起，您的资金不足！！！")




                                #购买采矿车情况
                                elif num == 7:
                                    #有无优惠券判断
                                    if be2 == 0:
                                        print("存在优惠券是否使用》》》【1、是】【2、否】")
                                        tqtk = int(input(":"))
                                        #是否使用优惠券判断
                                        if tqtk == 1:
                                            be2 = be2 + 1
                                            if money >= shop[num][1]:
                                                money = money - shop2[1]
                                                shopcar.append(shop2)
                                                print("购买成功！！！")
                                                print("您的当前余额为：",money)
                                            else:
                                                print("对不起，您的资金不足！！！")
                                        # else:
                                        #     print("已使用过优惠券，暂无优惠券！！！")
                                        elif tqtk == 2:
                                            if money >= shop[num][1]:
                                                money = money - shop[num][1]
                                                shopcar.append(shop[num])
                                                print("购买成功！！！")
                                                print("您的当前余额为：",money)
                                            else:
                                                print("对不起，您的资金不足！！！")

                                        else:
                                            print("输入非法！！！")
                                    else:
                                        if money >= shop[num][1]:
                                            money = money - shop[num][1]
                                            shopcar.append(shop[num])
                                            print("购买成功！！！")
                                            print("您的当前余额为：",money)
                                        else:
                                            print("对不起，您的资金不足！！！")


                                else:
                                    if money >= shop[num][1]:
                                        money = money - shop[num][1]
                                        shopcar.append(shop[num])
                                        print("购买成功！！！")
                                        print("您的当前余额为：",money)
                                    else:
                                        print("对不起，您的资金不足！！！")
                            else:
                                print("该商品不存在！！！！！")

                        elif num == "Q" or num == "q":
                            print("退出商城！！！")
                            break

                        else:
                            print("输入非法！！！！！")

                    #都卖完了需要输出一下购物清单
                    print("---------购物小票详情----------")
                    for index,value in enumerate(shopcar):
                        print(index,"    ",value)
                    print("您的当前余额为：",money)
                    print("您本次消费累计积分：",(money1 - money)/10)
                    print("【欢迎下次光临！！！】")

                elif num4 == "公司":
                    print("到达目的地！！！")
                elif num4 == "电影院":
                    print("到达目的地！！！")
                else:
                    print("没有您输入的地方！！！瞎了？")



            elif num3 == "q" or num3 == "Q":
                print("退出旅游导航！！！")
                break
            else:
                print("没有您输入的地方！！！瞎了？")

        elif num2 == "q" or num2 == "Q":
            print("退出旅游导航！！！")
            break
        else:
            print("没有您输入的区域！！！瞎了？")

    elif num1 == "q" or num1 == "Q":
        print("退出旅游导航！！！")
        break
    else:
        print("没有您输入的城市！！！瞎了？")


























