import unittest
from os import path
from datetime import date

from import_data import ImportAPdata

class TestImportMethods(unittest.TestCase):

    def test_apimport(self):
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportAPdata()
        ap.ImportData(path.join(test_data_path, '121.csv'))
        self.assertEqual(ap.columns['ACCOUNT'][1], 0)
        self.assertEqual(ap.columns['IDATE'][1], 3)
        self.assertEqual(ap.columns['REFNO'][1], 4)
        self.assertEqual(ap.columns['JOURNAL'][1], 5)
        self.assertEqual(ap.columns['AMOUNT'][1], 7)
        self.assertEqual(ap.ConvertDate("08/01/2018"), date(2018, 8, 1))



# from .models import Dept
#
# class DeptTestCase(TestCase):
#     def setUp(self):
#         Dept.objects.

if __name__ == '__main__':
     unittest.main()
