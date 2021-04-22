#1号水果
id1 = 1
name1 = "苹果"
price1 = 5.6
num1 = 100
quality1 = "A+"
address1 = "烟台"

#2号水果
id2 = 2
name2 = "香蕉"
price2 = 3.6
num2 = 200
quality2 = "B+"
address2 = "海南"

print("-------------------------------------------------------------")
print("---------------------- 欢迎来到水果商城 ------------------------")
print("-------------------------------------------------------------")
print("编号\t\t 名称\t\t 价格\t\t 数量\t\t品质\t\t\t出产地")
print(id1,"\t\t",name1,"\t\t",price1,"\t\t",num1,"\t\t",quality1,"\t\t",address1)
print(id2,"\t\t",name2,"\t\t",price2,"\t\t",num2,"\t\t",quality2,"\t\t",address2)
print("-------------------------------------------------------------")
print("总金额为：￥",price1 * num1 + price2 * num2)