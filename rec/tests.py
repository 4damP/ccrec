import unittest
from os import path
from datetime import datetime


from import_data import ImportData

class TestImportMethods(unittest.TestCase):
    def setup():
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportData()
        transactions = ap.ImportData(path.join(test_data_path, '121.csv'))

    def test_columns(self):
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportData()
        transactions = ap.ImportAPData(path.join(test_data_path, '121.csv'))
        self.assertEqual(ap.columns['ACCOUNT'][1], 0)
        self.assertEqual(ap.columns['IDATE'][1], 3)
        self.assertEqual(ap.columns['REFNO'][1], 4)
        self.assertEqual(ap.columns['JOURNAL'][1], 5)
        self.assertEqual(ap.columns['AMOUNT'][1], 7)

    def test_apdata(self):
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportData()
        transactions = ap.ImportAPData(path.join(test_data_path, '121.csv'))
        trans_list=[
            ['10', '894378', 20.00, "08/01/2018", 'SA', 'CC'],
            ['10', '894379', 31.47, "08/01/2018", 'SA', 'CC'],
            ]
        for each in trans_list:
            tr = transactions[each[0]][each[1]]
            tr[0] = f'{round(float(tr[0]),2):.2f}'
            tr[1] = datetime.strftime(tr[1], "%m/%d/%Y")
            test_amount = f'{each[2]:.2f}'
            test_date = each[3]
            journal = each[4]
            card_type = each[5]
            self.assertEqual(tr, [test_amount, test_date, journal, card_type])

    def test_gcdata(self):
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportData()
        transactions = ap.ImportAPData(path.join(test_data_path, '2081.csv'))
        trans_list=[
            ['20', '125388', -75.00, "08/29/2018", 'SA', 'GCR'],
            ['87', '7648',    50.00, "09/27/2018", 'SD', 'GCR'],
            ]
        for each in trans_list:
            tr = transactions[each[0]][each[1]]
            tr[0] = f'{round(float(tr[0]),2):.2f}'
            tr[1] = datetime.strftime(tr[1], "%m/%d/%Y")
            test_amount = f'{each[2]:.2f}'
            test_date = each[3]
            journal = each[4]
            card_type = each[5]
            self.assertEqual(tr, [test_amount, test_date, journal, card_type])

    def test_columns(self):
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        chs = ImportData()
        transactions = chs.ImportCHSData(path.join(test_data_path, 'TransactionDetail.csv'))
        self.assertEqual(chs.columns['Tran Date'][1], 0)
        self.assertEqual(chs.columns['Batch Date'][1], 1)
        self.assertEqual(chs.columns['Card Type'][1], 4)
        self.assertEqual(chs.columns['Tran Amount'][1], 6)
        self.assertEqual(chs.columns['Tran Type'][1], 7)
        self.assertEqual(chs.columns['Auth Code'][1], 10)

    def test_chscolumns(self):
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        chs = ImportData()
        transactions = chs.ImportCHSData(path.join(test_data_path, 'TransactionDetail.csv'))
        trans_list = [
            []
        ]
    #     transactions = ap.ImportData(path.join(test_data_path, 'TransactionDetail.csv'))
    #     self.assertEqual(ap.columns['ACCOUNT'][1], 0)
    #     self.assertEqual(ap.columns['IDATE'][1], 3)
    #     self.assertEqual(ap.columns['REFNO'][1], 4)
    #     self.assertEqual(ap.columns['JOURNAL'][1], 5)
    #     self.assertEqual(ap.columns['AMOUNT'][1], 7)
    #
    #
    # def test_chsdata(self):
    #     test_data_path = '/home/adam/projects/cc_rec/test_data'
    #     ap = ImportCHSdata()
    #     transactions = ap.ImportData(path.join(test_data_path, 'TransactionDetail.csv'))
    #     trans_list=[
    #         ['070009-000', '7/30/2018', 'WEX', 77.35, 'Sale', 'O', '236186'],
    #         ['800641-000', '8/30/2018', 'VSO', 12.25, 'Sale', 'O', '239251'],
    #         ]
    #     for each in trans_list:
    #         tr = transactions[each[0]][each[1]]
    #         tr[0] = f'{round(float(tr[0]),2):.2f}'
    #         test_amount = f'{each[2]:.2f}'
    #         test_date = each[3]
    #         journal = each[4]
    #         card_type = each[5]
    #         self.assertEqual(tr, [test_amount, test_date, journal, card_type])



# from .models import Dept
#
# class DeptTestCase(TestCase):
#     def setUp(self):
#         Dept.objects.

if __name__ == '__main__':
     unittest.main()
