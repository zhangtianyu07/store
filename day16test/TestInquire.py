import unittest
from Bank_addUser import Bank
from Address import Address
from User import User

class TestInquire(unittest.TestCase):

    user = None
    bank = None

    def setUp(self) -> None:
        self.user = User()
        self.bank = Bank()

    def test_Inquire(self):
        self.user.setAccount("12345671")
        self.user.setPassword(123450)

        JG = 0

        status5 = self.bank.bank_inquire(self.user.getAccount(),self.user.getPassword())
        status5 = int(status5)

        self.assertEqual(JG,status5)

    def test_Inquire1(self):
        self.user.setAccount("12345699")
        self.user.setPassword(123450)

        JG = 1

        status5 = self.bank.bank_inquire(self.user.getAccount(),self.user.getPassword())
        status5 = int(status5)

        self.assertEqual(JG,status5)

    def test_Inquire2(self):
        self.user.setAccount("12345671")
        self.user.setPassword(123459)

        JG = 2

        status5 = self.bank.bank_inquire(self.user.getAccount(),self.user.getPassword())
        status5 = int(status5)

        self.assertEqual(JG,status5)