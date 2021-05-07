import random
from DBUtils import update
from DBUtils import select
# 1. 空的银行的库 ： 100个
users = {}

# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    #查询数据库中是否存在账号

    sql = "select count(*) from bank"
    data = select(sql,[])  # ((72),(),())
    print(data)
    # 判断是否已满
    if data[0][0] >= 100:
        return 3

    sql1 = "select * from bank where account = %s"
    data1 = select(sql1,account)
    # 判断是否存在
    if len(data1) != 0:
        return 2

    # 准备一条sql语句
    sql2 = "insert into bank  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,0,bank_name]
    # 让控制台执行sql
    update(sql2,param2)
    return 1


# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")

#2.	存钱（传入值：用户的账号、存取的金额。返回值：布尔类型值）
# a)	业务逻辑：
# 	先根据传入的账号信息查询用户库里是否有该用户。若没有则返回False
# 	若有，则将该用户的金额存进去。

#银行的存钱逻辑
def bank_deposit(account,money):
    #判断有无账户存在

    sql3 = "select count(*) from bank where bank.account = %s"
    param3 = [account]
    data3 = select(sql3,param3)

    if data3[0][0] == 1:
        sql4 = "update bank set money = money + %s where account = %s"
        param4 = [money,account]
        update(sql4,param4)
        return True
    else:
        # print("账户不存在！！！")
        return False


#用户存钱方法
def deposit():

    account = str(input("请输入您要存储的账号："))

    money = input("请输入您要存储的金额为：")

    status2 = bank_deposit(account,money)

    if status2 == True:
        print("恭喜存入成功！")

    if status2 == False:
        print("存入失败！！！")


#3.	取钱（传入值：用户的账号，用户密码，取钱金额。返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
# a)	业务逻辑：
# 	先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
# 	若存在，则继续判断密码是否正确，若不正确，则返回代号2。
# 	若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
# 	若满足，则将该用户的金额减去。

#银行的取钱逻辑
def bank_withdraw(account,password,withdraw_money):
    #数据库

    sql5 = "select count(*) from bank where bank.account = %s"
    param5 = [account]
    data5 = select(sql5,param5)

    if data5[0][0] == 1:#存在
        sql6 = "select count(*) from bank where bank.account = %s and bank.password = %s"
        param6 = [account,password]
        data6 = select(sql6,param6)

        if data6[0][0] == 1:
            sqldx = "select * from bank where bank.account = %s"
            paramdx = [account]
            datadx = select(sqldx,paramdx)
            num = datadx[0][7]
            if num >= withdraw_money:
                sql7 = "update bank set bank.money =bank.money - %s where bank.money >= %s"
                param7 = [withdraw_money,withdraw_money]
                data7 = update(sql7,param7)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


#用户取钱的方法
def withdraw():

    account = input("请输入您要取钱的账号：")
    password = input("请输入您的密码:")
    withdraw_money = float(input("请输入您要取出的金额为："))

    status3 = bank_withdraw(account,password,withdraw_money)

    if status3 == 0:
        print("恭喜您取钱成功！！！")
        print("您的取出金额为：",withdraw_money)

    if status3 == 1:
        print("账号不存在!!!")

    if status3 == 2:
        print("密码不对!!!")

    if status3 == 3:
        print("钱不够!!!")


#4.	转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
# a)	业务逻辑：
# 	先查询用户库是否存在转出和转入的账号，若不存在则返回代号,1，
# 	若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
# 	若正确则继续判断要转出的金额是否足够，若不够则返回3，
# 	否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。

#银行的转账逻辑
def bank_ransferA(chu_account,ru_account,password,chu_money):
    sql8 = "select count(account) from bank where bank.account = %s or bank.account = %s"
    param8 = [chu_account,ru_account]
    data8 = select(sql8,param8)

    if data8[0][0] == 2:
        sql9 = "select count(account) from bank where bank.account = %s and bank.password = %s"
        param9 = [chu_account,password]
        data9 = select(sql9,param9)
        if data9[0][0] == 1:
            sqldx1 = "select * from bank where bank.account = %s"
            paramdx1 = [chu_account]
            datadx = select(sqldx1,paramdx1)
            num1 = datadx[0][7]
            if num1 >= chu_money:
                sql10 = "update bank set bank.money = bank.money - %s where bank.account = %s"
                param10 = [chu_money,chu_account]
                update(sql10,param10)
                sql11 = "update bank set bank.money = bank.money + %s where bank.account = %s"
                param11 = [chu_money,ru_account]
                update(sql11,param11)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


#用户转账方法
def ransferA():
    chu_account = input("请输入转出的账号：")
    ru_account = input("请输入转入的账号：")
    password = input("请输入您的密码:")
    chu_money = float(input("请输入您要转出的金额为："))

    status3 = bank_ransferA(chu_account,ru_account,password,chu_money)

    if status3 == 0:
        print("转账成功！！！")

    if status3 == 1:
        print("转出和转入的账号不存在！")

    if status3 == 2:
        print("转出账号的密码不正确！！")

    if status3 == 3:
        print("转出的金额不够！！！")


#5.	查询账户功能（传入值：账号，账号密码，返回值：空）
# a)	业务逻辑：
# 	先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
# 	否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
# 	若账号和密码都正确，则将该用户的信息都打印出来，
# 比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.

#银行的查询逻辑
def bank_inquire(account,password):
    sql12 = "select count(*) from bank where bank.account = %s"
    param12 = [account]
    data12 = select(sql12,param12)
    if data12[0][0] == 1:
        sql13 = "select count(*) from bank where bank.account = %s and bank.password = %s"
        param13 = [account,password]
        data13 = select(sql13,param13)

        if data13[0][0] == 1:
            return 0
        else:
            return 2
    else:
        return 1


#用户的查询方法
def inquire():
    account = input("请输入您要查询的账号：")
    password = input("请输入您的密码:")
    status4 = bank_inquire(account,password)

    if status4 == 0:
        sql14 = "select * from bank where bank.account = %s"
        param14 = [account]
        data14 = select(sql14,param14)
        for i in data14:
            account = data14[0][0]
            username = data14[0][1]
            password = data14[0][2]
            country = data14[0][3]
            province = data14[0][4]
            street = data14[0][5]
            door = data14[0][6]
            money = data14[0][7]
            bank_name = data14[0][8]

            print("当前账号信息：")
            info = '''
                ------------个人信息----------------
                当前当前账号：%s,
                用户名：%s,
                取款密码：%s,
                地址信息：
                    国家：%s,
                    省份：%s,
                    街道：%s,
                    门牌号：%s,
                余额：%s,
                开户行：%s
                -----------------------------------
            '''

            print(info % (account,username,password,country,province,street,door,money,bank_name))

    if status4 == 1:
        print("该用户不存在!!!")

    if status4 == 2:
        print("密码不正确！！！")


while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            deposit()
        elif num == 3:
            withdraw()
        elif num == 4:
            ransferA()
        elif num == 5:
            inquire()
        elif num == 6:
            print("拜拜了您嘞，欢迎下次光临！！！")
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")