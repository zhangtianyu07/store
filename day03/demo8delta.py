a = int(input("三角形a边为："))
b = int(input("三角形b边为："))
c = int(input("三角形c边为："))

#判断三角形
# if a+b>c or a+c>b or b+c>a and a==b!=c or b==c!=a or a==c!=b and a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
#     print("三角形是等腰直角三角形")
if (a+b>c or a+c>b or b+c>a) and (a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b):
    print("三角形是直角三角形")
elif (a+b>c or a+c>b or b+c>a) and (a==b!=c or b==c!=a or a==c!=b):
    print("三角形是等腰三角形")
elif (a+b>c or a+c>b or b+c>a) and a==b==c:
    print("三角形是等边三角形")
elif (a+b>c and c>a and c>b) or (a+c>b and b>a and b>c) or (b+c>a and a>b and a>c):
    print("三角形是普通三角形")
else:
    print("不构成三角形")