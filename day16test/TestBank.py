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

    def test_AddUser(self):
        # 1.准备测试数据
        self.user.setAccount("asd12345")
        self.user.setUsername("zyu")
        self.user.setPassword(123456)
        self.address.setCountry("中国")
        self.address.setProvince("中国")
        self.address.setStreet("中国")
        self.address.setDoor("s008")

        #预期结果
        JG = 1
        # 调用被测方法
        status = self.bank.bank_addUser(self.user.getAccount(),self.user.getUsername(),self.user.getPassword(),self.address.getCountry(),self.address.getProvince(),self.address.getStreet(),self.address.getDoor())
        status = int(status)

        # 断言
        self.assertEqual(JG,status)

    def test_AddUser1(self):
        # 1.准备测试数据
        self.user.setAccount("12345670")
        self.user.setUsername("zyu")
        self.user.setPassword(123456)
        self.address.setCountry("中国")
        self.address.setProvince("中国")
        self.address.setStreet("中国")
        self.address.setDoor("s008")

        #预期结果
        JG = 2
        # 调用被测方法
        status = self.bank.bank_addUser(self.user.getAccount(),self.user.getUsername(),self.user.getPassword(),self.address.getCountry(),self.address.getProvince(),self.address.getStreet(),self.address.getDoor())
        status = int(status)

        # 断言
        self.assertEqual(JG,status)

    # def test_AddUser2(self):
    #     # 1.准备测试数据
    #     self.user.setAccount("12345670")
    #     self.user.setUsername("zyu")
    #     self.user.setPassword(123456)
    #     self.address.setCountry("中国")
    #     self.address.setProvince("中国")
    #     self.address.setStreet("中国")
    #     self.address.setDoor("s008")
    #
    #     #预期结果
    #     JG = 2
    #     # 调用被测方法
    #     status = self.bank.bank_addUser(self.user.getAccount(),self.user.getUsername(),self.user.getPassword(),self.address.getCountry(),self.address.getProvince(),self.address.getStreet(),self.address.getDoor())
    #     status = int(status)
    #
    #     # 断言
    #     self.assertEqual(JG,status)

    def test_AddUser3(self):
        # 1.准备测试数据
        self.user.setAccount("12345670")
        self.user.setUsername("zyu")
        self.user.setPassword(123456)
        self.address.setCountry("中国")
        self.address.setProvince("中国")
        self.address.setStreet("中国")
        self.address.setDoor("s008")

        #预期结果
        JG = 3
        # 调用被测方法
        status = self.bank.bank_addUser(self.user.getAccount(),self.user.getUsername(),self.user.getPassword(),self.address.getCountry(),self.address.getProvince(),self.address.getStreet(),self.address.getDoor())
        status = int(status)

        # 断言
        self.assertEqual(JG,status)









