#声明一个列表，在列表中保存6个学生的信息(6个题1中的字典)
'''
students = [
     {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
     {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
     {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
     {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
     {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
     {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
 ]
 1)	统计不及格学生的个数
 2)	统计未成年学生的个数
 3)	打印手机尾号是8的学生的名字
 4)	打印最高分和对应的学生的名字
 5)	将列表按学生成绩从大到小排序
 6)	删除性别保密的所有学生
'''

students = [{'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
            {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
            {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
            {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
            {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
            {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
            ]

sco = 0
agee = 0
end = 0
a = 0
max_sco = 0
gender_name = 0
max_name = 0
students1 = []
#1)	统计不及格学生的个数
for i in students:
    if i["score"] < 60:
        sco = sco + 1
print("不及格学生的个数是：",sco)

#2)	统计未成年学生的个数
for i in students:
    if i["age"] < 18:
        agee = agee + 1
print("不及格学生的个数是：",agee)

#3)	打印手机尾号是8的学生的名字
for i in students:
    end = i["tel"]
    a = int(end[-1])
    if a % 8 == 0:
        end = i["name"]
        print("尾号为8的学生的名字为：",end)

#4)	打印最高分和对应的学生的名字
max_sco = i["score"]
for i in students:
    if max_sco <= i["score"]:
        max_sco = i["score"]
        max_name = i["name"]
print("最高分和对应的学生的名字为：",max_name)

#5)	将列表按学生成绩从大到小排序
import operator
students2 = []
students2 = sorted(students,key=operator.itemgetter('score'))
print("列表按学生成绩从大到小排序为：",format(students2))

#6)	删除性别保密的所有学生
print("删除性别保密的所有学生后：")
for i in students:
    if i["gender"] == "保密":
        del [i]
    else:
        print(i)







