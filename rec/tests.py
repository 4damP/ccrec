import unittest
from os import path
from datetime import datetime


from import_data import ImportData

class TestImportMethods(unittest.TestCase):
    def setup():
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportData()
        transactions = ap.ImportData(path.join(test_data_path, '121.csv'))

    def test_apcolumns(self):
        print('\r\nTesting AP columns are corrected...')
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportData()
        transactions = ap.ImportAPData(path.join(test_data_path, '121.csv'))
        self.assertEqual(ap.columns['ACCOUNT'][1], 0)
        self.assertEqual(ap.columns['IDATE'][1], 3)
        self.assertEqual(ap.columns['REFNO'][1], 4)
        self.assertEqual(ap.columns['JOURNAL'][1], 5)
        self.assertEqual(ap.columns['AMOUNT'][1], 7)

    def test_apdata(self):
        print('\r\nTesting AP data...')
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportData()
        transactions = ap.ImportAPData(path.join(test_data_path, '121.csv'))
        dept_totals = {}
        for dept in transactions:
            for refno in transactions[dept]:
                if dept not in dept_totals:
                    dept_totals[dept] = transactions[dept][refno][0]
                else:
                    dept_totals[dept] += transactions[dept][refno][0]
        test_totals = {'10': 22587.44, '12': 54136.83, '20': 54136.83, '22': 205675.54, '23': 957.16,\
                       '32': 2338.68, '40': 54618.67, '42': 51816.23, '43': 27937.75,\
                       '50': 61926.51, '52': 59067.92, '55': 1570.17, '56': 16736.88,\
                       '60': 125798.09, '62': 157282.82, '65': 3105.06, '66': 601.49, '68': 3999.97,\
                       '80': 109920.19, '82': 260519.98, '85': 311.85, '87': 51825.55, '90': -142.86,}

        for dept_no in test_totals:
            self.assertEqual(test_totals[dept_no], test_totals[str(dept_no)])

    def test_gcdata(self):
        print('\r\nTesting gift card data...')
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        ap = ImportData()
        transactions = ap.ImportAPData(path.join(test_data_path, '2081.csv'))
        dept_totals = {}
        for dept in transactions:
            for refno in transactions[dept]:
                if dept not in dept_totals:
                    dept_totals[dept] = transactions[dept][refno][0]
                else:
                    dept_totals[dept] += transactions[dept][refno][0]
        test_totals = {'20': -75, '40': -30, '60': -530, '80': -180}

        for dept_no in test_totals:
            self.assertEqual(test_totals[dept_no], test_totals[str(dept_no)])

    def test_chscolumns(self):
        print('\r\nTesting chs columns are corrected...')
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
        print('\r\nTesting CHS totals are correct...')
        test_data_path = '/home/adam/projects/cc_rec/test_data'
        chs = ImportData()
        transactions = chs.ImportCHSData(path.join(test_data_path, 'TransactionDetail.csv'))
        trans_totals = {}
        for trans in transactions:
            # print(trans[0], trans_totals)
            if trans[0] not in trans_totals:
                trans_totals[trans[0]] = trans[4]
            else:
                trans_totals[trans[0]] += trans[4]
        test_totals = {'070130-000': 49434.13,
                       '071423-000': 105891.87,
                       '071546-000': 282445.95,
                       '800641-000': 28316.73,
                       '070009-000': 365066.55,
                       '070025-000': 122509.05,
                       '070025-001': 23151.56,
                       '070025-002': 43062.63,
                       '070025-003': 2003.59,
                       '070025-004': 3961.00,
                       '070025-005': 268311.00,
                       '070025-006': 10806.86,
                }
        for merch_id in test_totals:
            amount = round(float(trans_totals[merch_id]), 2)
        self.assertEqual(test_totals[merch_id], amount)


if __name__ == '__main__':
     unittest.main()
