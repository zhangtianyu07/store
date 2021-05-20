import unittest
from Bank_addUser import Bank
from Address import Address
from User import User

class TestDeposit(unittest.TestCase):

    bank = None
    user = None

    def setUp(self) -> None:
        self.bank = Bank()
        self.user = User()

    def test_Deposit(self):
        #1、准备测试数据
        self.user.setAccount("asd12345")
        self.bank.setMoney(100)

        #预期结果
        JG = True
        #调用被测方法
        status2 = self.bank.bank_deposit(self.user.getAccount(),self.bank.getMoney())
        status2 = int(status2)

        #断言
        self.assertEqual(JG,status2)

    def test_Deposit1(self):
        #1、准备测试数据
        self.user.setAccount("12121345")
        self.bank.setMoney(100)

        #预期结果
        JG = False
        #调用被测方法
        status2 = self.bank.bank_deposit(self.user.getAccount(),self.bank.getMoney())
        status2 = int(status2)

        #断言
        self.assertEqual(JG,status2)





































