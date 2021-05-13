'''
    ["黑鹰战机",1500],
    ["天启坦克",3000],
    ["核潜艇",2000],
    ["乌贼战舰",1000],
    ["自爆卡车",1500],
    ["雇佣兵",200],
    ["猎犬",100],
    ["采矿车",1200],
    ["恐怖机器人",500],
    ["尤里",800],
'''
import  xlwt

# 空的工作簿
wb = xlwt.Workbook()

# 添加
sheet = wb.add_sheet("商城")

# 向选项卡里添加数据
sheet.write(0,0,"黑鹰战机")
sheet.write(0,1,1500)
sheet.write(1,0,"天启坦克")
sheet.write(1,1,3000)
sheet.write(2,0,"核潜艇")
sheet.write(2,1,2000)
sheet.write(3,0,"乌贼战舰")
sheet.write(3,1,1000)
sheet.write(4,0,"自爆卡车")
sheet.write(4,1,1500)
sheet.write(5,0,"雇佣兵")
sheet.write(5,1,200)
sheet.write(6,0,"猎犬")
sheet.write(6,1,100)
sheet.write(7,0,"采矿车")
sheet.write(7,1,1200)
sheet.write(8,0,"恐怖机器人")
sheet.write(8,1,500)
sheet.write(9,0,"尤里")
sheet.write(9,1,800)



# 保存
wb.save("商城库.xlsx")