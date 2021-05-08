#使用python复制一张图片到D盘的python文件夹里。

f1 = open(file="呸.jpg",mode="rb")
f2 = open(file="D:\python\呸.jpg",mode="wb")

data = f1.read()
f2.write(data)

f2.close()
f1.close()