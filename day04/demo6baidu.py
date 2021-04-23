#请编程统计列表中的每个数字出现的次数
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]

list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a = len(list)
b = 1
c = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0
while True:
    if c < a:
        a = a - 1
        if list[a-1] == 1:
            num1 = num1 + 1
        elif list[a-1] == 2:
            num2 = num2 + 1
        elif list[a-1] == 3:
            num3 = num3 + 1
        elif list[a-1] == 4:
            num4 = num4 + 1
        elif list[a-1] == 5:
            num5 = num5 + 1
        elif list[a-1] == 6:
            num6 = num6 + 1
        elif list[a-1] == 7:
            num7 = num7 + 1
        elif list[a-1] == 8:
            num8 = num8 + 1
        elif list[a-1] == 9:
            num9 = num9 + 1
        elif list[a-1] == 10:
            num10 = num10 + 1
    else:
        print("数字1出现了",num1,"次")
        print("数字2出现了",num2,"次")
        print("数字3出现了",num3,"次")
        print("数字4出现了",num4,"次")
        print("数字5出现了",num5,"次")
        print("数字6出现了",num6,"次")
        print("数字7出现了",num7,"次")
        print("数字8出现了",num8,"次")
        print("数字9出现了",num9,"次")
        print("数字10出现了",num10,"次")
        break