#写一个数据库DBUtils与Excel表的数据转换工具
# Db_to_excel() : 将数据库数据写入excel表里

from DBUtils import Mysql
import xlwt
ku = []
class Db_to_excel:
    sql = "select * from bank"
    data = Mysql.Select(sql,[])
    for i in data:
        i = list(i)
        ku.append(i)
    print(ku)


    #把数据库信息写入Excel表中
    # 空的工作簿
    wb = xlwt.Workbook()
    # 添加
    sheet = wb.add_sheet("用户管理")
    # 向选项卡里添加数据
    a = 0
    for i in range(len(ku)):

        for j in range(len(ku[i])):
            num = ku[i][j]

            sheet.write(i,j,num)

    # 保存
    wb.save("去往Excel表.xls")
