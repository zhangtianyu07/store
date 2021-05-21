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

@ddt
class TestCala(unittest.TestCase):
    @data(*ku)
    @unpack

    def test_add(self,a,b,c):
        cala = Calc()
        sum = float(cala.Add(a,b))
        c = float(c)
        self.assertEqual(c,sum)
























