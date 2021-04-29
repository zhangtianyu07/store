'''
语文 = ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']

1)	求选课学生总共有多少人
2)	求只选了第一个学科的人的数量和对应的名字
3)	求只选了一门学科的学生的数量和对应的名字
'''
c = 0
m = 0
e = 0
b = 0
#定义列表
chinese = ['小明','小张','小黄','小杨']
math = ['小黄','小李','小王','小杨','小周']
english = ['小杨','小张','小吴','小冯','小周']

#求选课学生总共有多少人
c = 0
list = []
for i in chinese:
    if i not in list:
        list.append(i)
        c = c + 1
for i in math:
    if i not in list:
        list.append(i)
        c = c + 1
for i in english:
    if i not in list:
        list.append(i)
        c = c + 1
print("选课学生总共有",c,"人")

#求只选了第一个学科的人的数量和对应的名字
for i in chinese:
    if i not in math and i not in english:
        print("只选了第一个学科的人:",i)
        b = b + 1
        print("只选了第一个学科的人的数量:",b)

#求只选了一门学科的学生的数量和对应的名字
b = 0
for i in chinese:
    if i not in math and i not in english:
        print("只选了一个学科的人:",i)
        b = b + 1
for i in math:
    if i not in chinese and i not in english:
        print("只选了一个学科的人:",i)
        b = b + 1
for i in english:
    if i not in math and i not in chinese:
        print("只选了一个学科的人:",i)
        b = b + 1
print("只选了一个学科的人的数量为：",b)





