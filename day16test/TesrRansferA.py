import unittest
from Bank_addUser import Bank
from Address import Address
from User import User

class TestRansferA(unittest.TestCase):

    bank = None
    user = None
    address = None

    def setUp(self) -> None:
        self.bank = Bank()
        self.user = User()
        self.address = Address()

    def test_RansferA(self):
        self.user.setAccount("12345670")
        self.user.setAccount("12345671")
        self.user.setPassword(123450)
        self.bank.setMoney(20)

        JG = 0

        status4 = self.bank.bank_withdraw(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())
        status4 = int(status4)

        self.assertEqual(JG,status4)

    def test_RansferA1(self):
        self.user.setAccount("12345699")
        self.user.setAccount("12345671")
        self.user.setPassword(123450)
        self.bank.setMoney(20)

        JG = 0

        status4 = self.bank.bank_withdraw(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())
        status4 = int(status4)

        self.assertEqual(JG,status4)

    def test_RansferA2(self):
        self.user.setAccount("12345670")
        self.user.setAccount("12345671")
        self.user.setPassword(123499)
        self.bank.setMoney(20)

        JG = 0

        status4 = self.bank.bank_withdraw(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())
        status4 = int(status4)

        self.assertEqual(JG,status4)

    def test_RansferA3(self):
        self.user.setAccount("12345670")
        self.user.setAccount("12345671")
        self.user.setPassword(123450)
        self.bank.setMoney(200)

        JG = 0

        status4 = self.bank.bank_withdraw(self.user.getAccount(),self.user.getPassword(),self.bank.getMoney())
        status4 = int(status4)

        self.assertEqual(JG,status4)













