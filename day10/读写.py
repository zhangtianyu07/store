'''
存储数据
    1、变量
    2、


1、打开资源
2、写入资源
3、关闭资源

'''

#file(输入资源名称)  mode(输入权限)  encoding(格式类型utf-8)
f = open(file="故事.txt",mode="r+",encoding="utf-8")

# f.write("草\n")
# f.write("作者：略\n")
# f.write("离离原上草\n")
# f.write("一岁一枯荣\n")
# f.write("野火烧不尽\n")
# f.write("春风吹又生\n")

print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()