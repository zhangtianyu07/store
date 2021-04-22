#井高度
num1 = 20
num2 = 0

while True:
    num1 = num1 - 3
    if num1 >= 0:
        num1 = num1 + 2
        num2 = num2 + 1
    else:
        break
print("一共花了",num2,"天")