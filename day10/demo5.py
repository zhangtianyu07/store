'''
现在有这样一个叫scores.txt的文件，里面有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
罗恩 23 35 44
哈利 60 77 68 88 90
赫敏 97 99 89 91 95 90
马尔福 100 85 90

希望你来统计这四个学生的魔法作业的总得分，然后再写入一个txt文件。
'''
user = []
users = []
sc = []
f = open(file="scores.txt",mode="r+",encoding="utf-8")
data = f.readlines()

f.close()
for i in data:
    da = i.split( )
    user.append(da)



for i in user:
    sum = 0
    for n in i[1:]:
        sun = int(n)
        sum = sum + sun
    print(sum)
    users.append(i[0])
    users.append(sum)
print(users)

# 打开 : 句柄，把柄
f = open(file="sc.txt",mode="w+",encoding="utf-8")

# 写个数据
b = 0
for i in users:
    a = str(i)
    f.write(a)
    b = b + 1
    if b%2 == 0:
        f.write("\n")




# print(f.read())  # 禁止使用
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
f.readlines() # ["静夜思","【李白】",""]

# 关闭资源
f.close()

# 任务：将《静夜思》  拷贝一份  到b.txt文件里



















