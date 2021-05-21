'''
参数化
引入包

'''

#引入包
import unittest
from JSQ import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

#数据源
import unittest
import xlrd
from JSQ import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

ku = []

#取出excel中的数据
wb = xlrd.open_workbook(filename="ShuJv.xlsx",encoding_override=True)
sheet = wb.sheet_by_name("Sheet1")

rows = sheet.nrows
cols = sheet.ncols

for i in range(rows):
    ku.append(sheet.row_values(i))

#将测试类进行修饰

@ddt
class TestCala(unittest.TestCase):

    @data(*ku)
    @unpack
    def test_Add(self,a,b,c):
        cala = Calc()
        sum = cala.Add(a,b)
        self.assertEqual(c,sum)





















