import random
from Utils import Utils
from Address import Address
from welcome import Welcome
from User import User
from Utils import Utils
from DBUtils import Mysql


class Bank:

    #银行数据库
    users = {}

    bank_choose = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye!"}

    #银行
    __money = 0
    __bank_name = "工商银行昌平支行"

    def setMoney(self,money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def setBank_name(self,bank_name):
        self.__bank_name = bank_name

    def getBank_name(self):
        return self.__bank_name

    # 判断是否在某个范围之内
    def isExists(self,chose, data):
        if chose in data:
            return True
        return False

    #银行开户逻辑
    def bank_addUser(self,account,username,password,country,province,street,door):
        sql = "select count(*) from bank"
        data = Mysql.Select(sql,[])  # ((72),(),())
        if len(data) >= 100:
            return 3

        sql1 = "select * from bank where account = %s"
        data1 = Mysql.Select(sql1,account)
        # 判断是否存在
        if len(data1) != 0:
            return 2

        # 准备一条sql语句
        sql2 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [account,username,password,country,province,street,door,self.__money,self.__bank_name]
        # 让控制台执行sql
        Mysql.Update(sql2,param2)
        return 1

    #银行存款逻辑
    def bank_deposit(self,account,money):
        #判断有无账户存在

        sql3 = "select count(*) from bank where bank.account = %s"
        param3 = [account]
        data3 = Mysql.Select(sql3,param3)

        if data3[0][0] == 1:
            sql4 = "update bank set money = money + %s where account = %s"
            param4 = [money,account]
            Mysql.Update(sql4,param4)
            return True
        else:
            # print("账户不存在！！！")
            return False

    #银行取钱逻辑
    def bank_withdraw(self,account,password,withdraw_money):
        #数据库
        sql5 = "select count(*) from bank where bank.account = %s"
        param5 = [account]
        data5 = Mysql.Select(sql5,param5)

        if data5[0][0] == 1:#存在
            sql6 = "select count(*) from bank where bank.account = %s and bank.password = %s"
            param6 = [account,password]
            data6 = Mysql.Select(sql6,param6)

            if data6[0][0] == 1:
                sqldx = "select * from bank where bank.account = %s"
                paramdx = [account]
                datadx = Mysql.Select(sqldx,paramdx)
                num = datadx[0][7]
                if num >= withdraw_money:
                    sql7 = "update bank set bank.money =bank.money - %s where bank.money >= %s"
                    param7 = [withdraw_money,withdraw_money]
                    Mysql.Update(sql7,param7)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1

    #银行转账逻辑
    def bank_ransferA(self,chu_account,ru_account,password,chu_money):
        sql8 = "select count(account) from bank where bank.account = %s or bank.account = %s"
        param8 = [chu_account,ru_account]
        data8 = Mysql.Select(sql8,param8)

        if data8[0][0] == 2:
            sql9 = "select count(account) from bank where bank.account = %s and bank.password = %s"
            param9 = [chu_account,password]
            data9 = Mysql.Select(sql9,param9)
            if data9[0][0] == 1:
                sqldx1 = "select * from bank where bank.account = %s"
                paramdx1 = [chu_account]
                datadx = Mysql.Select(sqldx1,paramdx1)
                num1 = datadx[0][7]

                if num1 >= chu_money:
                    sql10 = "update bank set bank.money = bank.money - %s where bank.account = %s"
                    param10 = [chu_money,chu_account]
                    Mysql.Update(sql10,param10)
                    sql11 = "update bank set bank.money = bank.money + %s where bank.account = %s"
                    param11 = [chu_money,ru_account]
                    Mysql.Update(sql11,param11)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1


    #银行用户查询逻辑
    def bank_inquire(self,account,password):
        sql12 = "select count(*) from bank where bank.account = %s"
        param12 = [account]
        data12 = Mysql.Select(sql12,param12)
        if data12[0][0] == 1:
            sql13 = "select count(*) from bank where bank.account = %s and bank.password = %s"
            param13 = [account,password]
            data13 = Mysql.Select(sql13,param13)

            if data13[0][0] == 1:
                return 0
            else:
                return 2
        else:
            return 1





















# import random
# from DBUtils import Mysql
# #开户方法
# class AddUser:
#
#     def addUser(self,account,username,password,country,province,street,door,money,bank_name):
#         sql = "select count(*) from bank"
#         data = Mysql.Select(sql,[])  # ((72),(),())
#         if len(data) >= 100:
#             return 3
#
#         sql1 = "select * from bank where account = %s"
#         data1 = Mysql.Select(sql1,account)
#         # 判断是否存在
#         if len(data1) != 0:
#             return 2
#
#         # 准备一条sql语句
#         sql2 = "insert into bank  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         param2 = [account,username,password,country,province,street,door,0,self.__bank_name]
#         # 让控制台执行sql
#         Mysql.Update(sql2,param2)
#         return 1