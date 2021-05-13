# Excel_to_db(): 将excel表里的数据写入到数据库
import xlrd
from DBUtils import Mysql

ku = []

#读取
wb = xlrd.open_workbook(filename="去往数据库.xlsx",encoding_override=True)

#取表
sheet = wb.sheet_by_name("Sheet1")

#取列取行
rows = sheet.nrows
cols = sheet.ncols

for i in range(rows):
    ku.append(sheet.row_values(i))

for i in ku:
    num = int(i[0])
    del i[0]
    i.insert(0,str(num))
    num1 = int(i[2])
    del i[2]
    i.insert(2,str(num1))

for i in range(len(ku)):
    param = []
    for j in range(len(ku[i])):
        num = ku[i][j]
        param.append(num)
    sql = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    Mysql.Update(sql,param)