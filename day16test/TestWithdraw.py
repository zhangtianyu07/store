import unittest
from Bank_addUser import Bank
from Address import Address
from User import User

class TestAddUser(unittest.TestCase): # 类就是单元测试的子类

    bank = None
    user = None
    address = None

    def setUp(self) -> None:
        self.bank = Bank()
        self.user = User()
        self.address = Address()

    def test_Withdraw(self):
        self.user.setAccount("asd12345")
        self.user.setPassword(123456)
        self.bank.setMoney(20)

        JG = 0

        status3 = self.bank.bank_withdraw(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())
        status3 = int(status3)

        self.assertEqual(JG,status3)

    def test_Withdraw1(self):
        self.user.setAccount("88888345")
        self.user.setPassword(123456)
        self.bank.setMoney(20)

        JG = 1

        status3 = self.bank.bank_withdraw(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())
        status3 = int(status3)

        self.assertEqual(JG,status3)

    def test_Withdraw2(self):
        self.user.setAccount("asd12345")
        self.user.setPassword(223456)
        self.bank.setMoney(20)

        JG = 2

        status3 = self.bank.bank_withdraw(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())
        status3 = int(status3)

        self.assertEqual(JG,status3)

    def test_Withdraw3(self):
        self.user.setAccount("asd12345")
        self.user.setPassword(123456)
        self.bank.setMoney(500)

        JG = 3

        status3 = self.bank.bank_withdraw(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())
        status3 = int(status3)

        self.assertEqual(JG,status3)














