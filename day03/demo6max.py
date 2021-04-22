num = 0
num2 = 0
num3 = 0
while num < 10:
    num = num + 1
    num1 = int(input("请输入一个数："))
    num2 = num2 + num1
    if num3 > num1:
        num3 = num3
    else:
        num3 = num1
print("十个数的和为:",num2)
print("输入十个",num3)
print("十个数的平均数为：",num2 / num)