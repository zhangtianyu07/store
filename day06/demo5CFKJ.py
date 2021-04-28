#变成乘法口诀
b = 10
i = 0
n = 0
while n < 9:
    i = n
    n = n + 1
    a = 1
    b = b - 1
    while i < 9:
        print(a,"x",b,"=",a*b,end="\t")
        a = a + 1
        i = i + 1
    print("\n")

#变成乘法口诀
i = 9
while i > 0:
    j = 1
    while j <= i:
        print(j,"x",i,"=",i*j,end="\t")
        j = j + 1
    i = i - 1
    print("\n")