#有下列列表，请编程实现列表的数据翻转
# 可以选做list = [1,2,3,4,5,6,7,8,9]
# 实现效果：list = [9,8,7,6,5,4,3,2,1]

list = [1,2,3,4,5,6,7,8,9]
last = []
b = len(list)
c = 0
while c < len(list):
    last.append(list[b - 1])
    b = b - 1
    c = c + 1
list = last
print("list = ",list)