from Address import Address
from bank import Bank
from welcome import Welcome
from User import User
from Utils import Utils
from DBUtils import Mysql

#初始化必要的对象
welcome = Welcome()
utils = Utils()
address = Address()
user = User()
bank = Bank()


#用户开户
def addUser():
    account = utils.getRandom()
    user.setUsername(utils.inputHelp("用户名："))
    user.setPassword(utils.inputHelp("密码："))
    address.setCountry(utils.inputHelp("国家："))
    address.setProvince(utils.inputHelp("省份："))
    address.setStreet(utils.inputHelp("街道："))
    address.setDoor(utils.inputHelp("门牌号："))

    status = bank.bank_addUser(account,user.getUsername(),user.getPassword(),address.getCountry(),address.getProvince(),address.getStreet(),address.getDoor())
    if status == 1:
        print("恭喜开户成功！")
    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")

#用户存款
def deposit():

    account = utils.inputHelp("您要存款的账号：")

    bank.setMoney(utils.inputHelp("存款金额："))

    status2 = bank.bank_deposit(account,bank.getMoney())

    if status2 == True:
        print("恭喜存入成功！")

    if status2 == False:
        print("存入失败！！！")


#用户取款
def withdraw():

    account = utils.inputHelp("您要取款的账号：")
    user.setPassword(utils.inputHelp("您要取款账号的密码："))
    bank.setMoney(float(utils.inputHelp("您要取款的金额：")))

    status3 = bank.bank_withdraw(account,user.getPassword(),bank.getMoney())

    if status3 == 0:
        print("恭喜您取钱成功！！！")
        print("您的取出金额为：",bank.getMoney())

    if status3 == 1:
        print("账号不存在!!!")

    if status3 == 2:
        print("密码不对!!!")

    if status3 == 3:
        print("钱不够!!!")


#用户转账
def ransferA():
    chu_account = utils.inputHelp("转出的账号：")
    ru_account = utils.inputHelp("转入的账号：")
    user.setPassword(utils.inputHelp("密码："))
    bank.setMoney(float(utils.inputHelp("您要转账的金额：")))

    status3 = bank.bank_ransferA(chu_account,ru_account,user.getPassword(),bank.getMoney())

    if status3 == 0:
        print("转账成功！！！")

    if status3 == 1:
        print("转出和转入的账号不存在！")

    if status3 == 2:
        print("转出账号的密码不正确！！")

    if status3 == 3:
        print("转出的金额不够！！！")


#用户查询
def inquire():
    account = utils.inputHelp("转出的账号：")
    user.setPassword(utils.inputHelp("密码："))

    status4 = bank.bank_inquire(account,user.getPassword())

    if status4 == 0:
        sql14 = "select * from bank where bank.account = %s"
        param14 = [account]
        data14 = Mysql.Select(sql14,param14)
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
    #界面显示类
    welcome.welcome()
    #用户选择：1 2 3 4 5 6
    chose = utils.inputHelp("选择")

    if bank.isExists(chose,bank.bank_choose):
        if chose == "1":
            addUser()
        elif chose == "2":
            deposit()
        elif chose == "3":
            withdraw()
        elif chose == "4":
            ransferA()
        elif chose == "5":
            inquire()
        elif chose == "6":
            print("拜拜了您嘞，欢迎下次光临！！！")
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")