#将《12月衣服的销售数据》使用变量的方式存储，并进行计算每件衣服的销售占比，每种衣服的在本月的销售额占比，本月总销售额。并最终打印到控制台上

#1号服装
id1 = 1
name1 = "羽绒服"
price1 = 253.6
num1 = 500
sales1 = 10

#2号服装
id2 = 2
name2 = "牛仔裤"
price2 = 86.3
num2 = 600
sales2 = 60

#3号服装
id3 = 3
name3 = "风衣"
price3 = 96.8
num3 = 335
sales3 = 43

#4号服装
id4 = 4
name4 = "皮草"
price4 = 135.9
num4 = 855
sales4 = 63

#5号服装
id5 = 5
name5 = "T恤"
price5 = 65.8
num5 = 632
sales5= 63

#6号服装
id6 = 6
name6 = "衬衫"
price6 = 49.3
num6 = 562
sales6 = 120

#7号服装
id7 = 7
name7 = "羽绒服"
price7 = 86.3
num7 = 600
sales7 = 72

#8号服装
id8 = 8
name8 = "羽绒服"
price8 = 253.6
num8 = 500
sales8 = 69

#9号服装
id9 = 9
name9 = "牛仔裤"
price9 = 86.3
num9 = 600
sales9 = 35

#10号服装
id10 = 10
name10 = "羽绒服"
price10 = 253.6
num10 = 500
sales10 = 140

#11号服装
id11 = 11
name11 = "牛仔裤"
price11 = 86.3
num11 = 600
sales11 = 90

#12号服装
id12 = 12
name12 = "皮草"
price12 = 135.9
num12 = 855
sales12 = 24

#13号服装
id13 = 13
name13 = "T恤"
price13 = 65.8
num13 = 632
sales13 = 45

#14号服装
id14 = 14
name14 = "风衣"
price14 = 96.8
num14 = 335
sales14 = 25

#15号服装
id15 = 15
name15 = "牛仔裤"
price15 = 86.3
num15 = 600
sales15 = 60

#16号服装
id16 = 16
name16 = "T恤"
price16 = 65.8
num16 = 632
sales16 = 129

#17号服装
id17 = 17
name17 = "羽绒服"
price17 = 253.6
num17 = 500
sales17 = 10

#18号服装
id18 = 18
name18 = "风衣"
price18 = 96.8
num18 = 335
sales18 = 43

#19号服装
id19 = 5
name19 = "T恤"
price19 = 65.8
num19 = 632
sales19 = 63

#20号服装
id20 = 20
name20 = "牛仔裤"
price20 = 86.3
num20 = 600
sales20 = 60

#21号服装
id21 = 21
name21 = "皮草"
price21 = 135.9
num21 = 855
sales21 = 63

#22号服装
id22 = 22
name22 = "风衣"
price22 = 96.8
num22 = 335
sales22 = 60

#23号服装
id23 = 23
name23 = "T恤"
price23 = 65.8
num23 = 632
sales23= 58

#24号服装
id24 = 24
name24 = "牛仔裤"
price24 = 86.3
num24 = 600
sales24 = 140

#25号服装
id25 = 25
name25 = "T恤"
price25 = 65.8
num25 = 632
sales25= 48

#26号服装
id26 = 26
name26 = "风衣"
price26 = 96.8
num26 = 335
sales26 = 43

#27号服装
id27 = 27
name27 = "皮草"
price27 = 135.9
num27 = 855
sales27 = 57

#28号服装
id28 = 28
name28 = "羽绒服"
price28 = 253.6
num28 = 500
sales28 = 10

#29号服装
id29 = 29
name29 = "T恤"
price29 = 65.8
num29 = 632
sales29= 63

#30号服装
id30 = 30
name30 = "风衣"
price30 = 96.8
num30 = 335
sales30 = 78

#所有衣服总数
YFZSsales = num1 + num2 + num3 + num4 + num5 + num6

#本月总销售额
Zsales = price1 * sales1 + price2 * sales2 + price3 * sales3 + price4 * sales4 + price5 * sales5 + price6 * sales6 + price7 * sales7 + price8 * sales8 + price9 * sales9 + price10 * sales10 + price11 * sales11 + price12 * sales12 + price13 * sales13 + price14 * sales14 + price15 * sales15 + price16 * sales16 + price17 * sales17 + price18 * sales18 + price19 * sales19 +  price20 * sales20 + price21 * sales21 + price22 * sales22 + price23 * sales23 + price24 * sales24 + price25 * sales25 + price26 * sales26 + price27 * sales27 + price28 * sales28 + price29 * sales29 + price30 * sales30

#本月总销售服装件数
JSsales = sales1 + sales2 + sales3 + sales4 + sales5 + sales6 + sales7 + sales8 + sales9 + sales10 + sales11 + sales12 + sales13 + sales14 + sales15 + sales16 + sales17 + sales18 + sales19 + sales20 + sales21 + sales22 + sales23 + sales24 + sales25 + sales26 + sales27 + sales28 + sales29 + sales30

#羽绒服本月销售
YRFsales = price1 * sales1 + price8 * sales8 + price10 * sales10 + price17 * sales17 + price28 * sales28

#牛仔裤本月销售
NZKsales = price2 * sales2 + price7 * sales7 + price9 * sales9 + price11 * sales11 + price15 * sales15 + price20 * sales20 + price24 * sales24

#风衣本月销售
FYsales = price3 * sales3 + price14 * sales14 + price18 * sales18 + price22 * sales22 + price26 * sales26 + price30 * sales30

#皮草本月销售
PCsales = price4 * sales4 + price12 * sales12 + price21 * sales21 + price27 * sales27

#T恤本月销售
TXsales = price5 * sales5 + price13 * sales13 + price16 * sales16 + price19 * sales19 + price23 * sales23 + price25 * sales25 + price29 * sales29

#衬衫本月销售
CSsales = price6 * sales6

#12月销售数据
print("------------------------------------------------------")
print("--------------------12月份衣服销售数据-------------------")
print("------------------------------------------------------")
print("日期\t\t服装名称\t\t价格/件\t\t库存数量\t\t销售量/每日")
print(id1,"\t\t",name1,"\t\t",price1,"\t\t",num1,"\t\t",sales1)
print(id2,"\t\t",name2,"\t\t",price2,"\t\t",num2,"\t\t",sales2)
print(id3,"\t\t",name3,"\t\t",price3,"\t\t",num3,"\t\t",sales3)
print(id4,"\t\t",name4,"\t\t",price4,"\t\t",num4,"\t\t",sales4)
print(id5,"\t\t",name5,"\t\t",price5,"\t\t",num5,"\t\t",sales5)
print(id6,"\t\t",name6,"\t\t",price6,"\t\t",num6,"\t\t",sales6)
print(id7,"\t\t",name7,"\t\t",price7,"\t\t",num7,"\t\t",sales7)
print(id8,"\t\t",name8,"\t\t",price8,"\t\t",num8,"\t\t",sales8)
print(id9,"\t\t",name9,"\t\t",price9,"\t\t",num9,"\t\t",sales9)
print(id10,"\t\t",name10,"\t\t",price10,"\t\t",num10,"\t\t",sales10)
print(id11,"\t\t",name11,"\t\t",price11,"\t\t",num11,"\t\t",sales11)
print(id12,"\t\t",name12,"\t\t",price12,"\t\t",num12,"\t\t",sales12)
print(id13,"\t\t",name13,"\t\t",price13,"\t\t",num13,"\t\t",sales13)
print(id14,"\t\t",name14,"\t\t",price14,"\t\t",num14,"\t\t",sales14)
print(id15,"\t\t",name15,"\t\t",price15,"\t\t",num15,"\t\t",sales15)
print(id16,"\t\t",name16,"\t\t",price16,"\t\t",num16,"\t\t",sales16)
print(id17,"\t\t",name17,"\t\t",price17,"\t\t",num17,"\t\t",sales17)
print(id18,"\t\t",name18,"\t\t",price18,"\t\t",num18,"\t\t",sales18)
print(id19,"\t\t",name19,"\t\t",price19,"\t\t",num19,"\t\t",sales19)
print(id20,"\t\t",name20,"\t\t",price20,"\t\t",num20,"\t\t",sales20)
print(id21,"\t\t",name21,"\t\t",price21,"\t\t",num21,"\t\t",sales21)
print(id22,"\t\t",name22,"\t\t",price22,"\t\t",num22,"\t\t",sales22)
print(id23,"\t\t",name23,"\t\t",price23,"\t\t",num23,"\t\t",sales23)
print(id24,"\t\t",name24,"\t\t",price24,"\t\t",num24,"\t\t",sales24)
print(id25,"\t\t",name25,"\t\t",price25,"\t\t",num25,"\t\t",sales25)
print(id26,"\t\t",name26,"\t\t",price26,"\t\t",num26,"\t\t",sales26)
print(id27,"\t\t",name27,"\t\t",price27,"\t\t",num27,"\t\t",sales27)
print(id28,"\t\t",name28,"\t\t",price28,"\t\t",num28,"\t\t",sales28)
print(id29,"\t\t",name29,"\t\t",price29,"\t\t",num29,"\t\t",sales29)
print(id30,"\t\t",name30,"\t\t",price30,"\t\t",num30,"\t\t",sales30)
print("----------------------------------------------------")
print("每件衣服的销售占比:",JSsales / YFZSsales,"%")
print("羽绒服在本月的销售额占比：",YRFsales / Zsales * 100,"%")
print("牛仔裤在本月的销售额占比：",NZKsales / Zsales * 100,"%")
print("风衣在本月的销售额占比：",FYsales / Zsales * 100,"%")
print("皮草在本月的销售额占比：",PCsales / Zsales * 100,"%")
print("T恤在本月的销售额占比：",TXsales / Zsales * 100,"%")
print("衬衫在本月的销售额占比：",CSsales / Zsales * 100,"%")
print("本月总销售额：￥",Zsales)