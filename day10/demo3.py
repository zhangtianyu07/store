#编写程序模拟证件上传的功能，
# 让用户输入证件的路径，并拷贝到一个统一的图片路径下。
print("请输入您要选择的图片路径：")
tp = input(":")
sfzh = input("请输入您的身份证号：")

tp1 = "D:\python" + "/" + sfzh

f1 = open(file=tp,mode="rb")
f2 = open(file=tp1,mode="wb")

data = f1.read()
f2.write(data)

f2.close()
f1.close()