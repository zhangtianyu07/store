import unittest
from HTMLTestRunner import HTMLTestRunner
#1、创建测试集
suite = unittest.TestSuite()
#2、让测试加载器自己加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\LTpython\day16test",pattern="Test*.py")
#3、将所用例 放入测试集
suite.addTests(tests)
#4、创建测试运行器
f = open(file="银行测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = "这是一个银行测试报告！",
    verbosity = 2,
    description = "执行了五个测试点"
)
#5、让运行器生产测试报告

runner.run(suite)