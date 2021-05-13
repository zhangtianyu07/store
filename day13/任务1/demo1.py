import xlrd
import xlwt
#获取工作表
gzb = xlrd.open_workbook(filename="D:\LTpython\day13\任务\\12月份衣服销售数据.xlsx",encoding_override=True)

#获取表格
xxk = gzb.sheet_by_name("12月份各种服饰销售情况")

#获取行列
rows = xxk.nrows #获取行
cols = xxk.ncols #获取列

#定义初始变量
yrf = 0
nzk = 0
fy = 0
pc = 0
tx = 0
cs = 0
#销售量
yrfxsl = 0
nzkxsl = 0
fyxsl = 0
pcxsl = 0
txxsl = 0
csxsl = 0

num = 0

for i in range(rows)[1:]:
    # print(xxk.row_values(i))
    # print(xxk.row_values(i)[1])
    if xxk.row_values(i)[1] == "羽绒服":
        yrf = yrf + xxk.row_values(i)[2] * xxk.row_values(i)[4]
        yrfkc = xxk.row_values(i)[3]
        yrfxsl = xxk.row_values(i)[4] + yrfxsl
        num = num + 1

    elif xxk.row_values(i)[1] == "牛仔裤":
        nzk = nzk + xxk.row_values(i)[2] * xxk.row_values(i)[4]
        nzkkc = xxk.row_values(i)[3]
        nzkxsl = xxk.row_values(i)[4] + nzkxsl
        num = num + 1

    elif xxk.row_values(i)[1] == "风衣":
        fy = fy + xxk.row_values(i)[2] * xxk.row_values(i)[4]
        fykc = xxk.row_values(i)[3]
        fyxsl = xxk.row_values(i)[4] + fyxsl
        num = num + 1

    elif xxk.row_values(i)[1] == "皮草":
        pc = pc + xxk.row_values(i)[2] * xxk.row_values(i)[4]
        pckc = xxk.row_values(i)[3]
        pcxsl = xxk.row_values(i)[4] + pcxsl
        num = num + 1

    elif xxk.row_values(i)[1] == "T血":
        tx = tx + xxk.row_values(i)[2] * xxk.row_values(i)[4]
        txkc = xxk.row_values(i)[3]
        txxsl = xxk.row_values(i)[4] + txxsl
        num = num + 1

    else:
        cs = cs + xxk.row_values(i)[2] * xxk.row_values(i)[4]
        cskc = xxk.row_values(i)[3]
        csxsl = xxk.row_values(i)[4] + csxsl
        num = num + 1


#总销售额：198400.6
sum = yrf + nzk + fy + pc + tx + cs


#羽绒服本月销售占比
yrfz = yrfxsl / yrfkc * 100


#牛仔裤本月销售占比
nzkz = nzkxsl / nzkkc * 100
nzkz = round(nzkz,0)


#风衣本月销售占比
fyz = fyxsl / fykc * 100
fyz = round(fyz,0)


#皮草本月销售占比
pcz = pcxsl / pckc * 100
pcz = round(pcz,0)


#T血本月销售占比
txz = txxsl / txkc * 100
txz = round(txz,0)


#衬衫本月销售占比
csz = csxsl / cskc * 100
csz = round(csz,0)


#平均日销售量
ri = yrfxsl + nzkxsl + pcxsl+ fyxsl + txxsl + csxsl
ri = ri / num
ri = round(ri,0)



wb = xlwt.Workbook(encoding="utf-8")
# 添加
sheet = wb.add_sheet("用户管理")

for i in range(rows):
    for j in range(cols):
        zhi = xxk.cell_value(i,j)
        sheet.write(i,j,zhi)

sheet.write(num + 2,0,"总销售额：" + str(sum))
sheet.write(num + 2,3,"平均日销售量：" + str(ri))
sheet.write(num + 2,4,"羽绒服本月销售占比:" + str(yrfz))
sheet.write(num + 3,4,"牛仔裤本月销售占比:" + str(nzkz))
sheet.write(num + 4,4,"风衣本月销售占比:" + str(fyz))
sheet.write(num + 5,4,"皮草本月销售占比:" + str(pcz))
sheet.write(num + 6,4,"T血本月销售占比:" + str(txz))
sheet.write(num + 7,4,"衬衫本月销售占比:" + str(csz))

# 添加
sheet = wb.add_sheet("羽绒服")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"羽绒服")
sheet.write(1,1,str(yrfxsl))
# 添加
sheet = wb.add_sheet("牛仔裤")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"牛仔裤")
sheet.write(1,1,str(nzkxsl))
# 添加
sheet = wb.add_sheet("风衣")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"风衣")
sheet.write(1,1,str(fyxsl))
# 添加
sheet = wb.add_sheet("皮草")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"皮草")
sheet.write(1,1,str(pcxsl))
# 添加
sheet = wb.add_sheet("T血")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"T血")
sheet.write(1,1,str(txxsl))
# 添加
sheet = wb.add_sheet("衬衫")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"衬衫")
sheet.write(1,1,str(csxsl))

# 保存
wb.save("12月份各种服饰销售情况.xls")







































