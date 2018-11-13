import csv
from os import path
from datetime import datetime
from decimal import *
from xml.dom.minidom import parse
import xml.dom.minidom

# from .models import Dept

class ImportData():
    """
    Import data from csv files for credit card sales, gift card recharges,
    and payments for transactions.
    """

    def __init__(self):
        # configuration dictionaries to be stored in an xml file
        self.columns = self.GetColumnReference('config.xml')
        # implement ORM to get merchant id dictionary
        self.merchant_ids = {'070009-000': {'I': 80, 'O': 82},\
                             '070009-001': {'I': 80, 'O': 82},\
                             '800641-000': {'O': 43},\
                             '070025-000': {'I': 50, 'O': 52},\
                             '070025-001': {'I': 56},\
                             '070025-002': {'I': 87},\
                             '070025-003': {'I': 32},\
                             '070025-004': {'I': 68},\
                             '070025-005': {'I': 20, 'O': 22},\
                             '070025-006': {'I': 87},\
                             '070130-000': {'I': 10, 'O': 12},\
                             '071423-000': {'I': 40, 'O': 42},\
                             '071546-000': {'I': 60, 'O': 62},\
                     }

    def GetDeptsDict(self):
        try:
            depts = Dept.objects.order_by('dept_no')
            return
        except Exception as e:
            print(str(e))

    def GetColumnReference(self, filename):
        '''
        Map header columns based on config file.
        '''
        table_columns = {}
        dom = parse(filename)
        columns = dom.documentElement
        cols = columns.getElementsByTagName('column')
        for col in cols:
            title = col.getElementsByTagName('title')[0].childNodes[0].data
            header = col.getElementsByTagName('header')[0].childNodes[0].data
            table = col.getElementsByTagName('table')[0].childNodes[0].data
            csv_column = col.getElementsByTagName('csv_column')[0].childNodes[0].data
            table_columns[title] = [table, csv_column, header]
        return table_columns

    def MapHeaderToColumns(self, header):
        for each in header:
            for col in self.columns:
                if each in self.columns[col]:
                    self.columns[col][1] = header.index(each)

    def ConvertAmount(self, amount):
        """Deformat $ amount, remove extra symbols and convert to float."""
        # amt = amount.replace(',', '')
        try:
            if amount[0] == '(':
                amt = -1 * (float(amount.strip('()').strip('$').replace(',', '')))
            else:
                amt = float(amount.strip('$').replace(',', ''))
            return amt
        except ValueError as e:
            print(str(e))

    def ImportAPData(self, filename):
        transactions = {}
        with open(filename, 'r', encoding='utf-8-sig') as filename:
            csvreader = csv.reader(filename)
            self.MapHeaderToColumns(next(csvreader, None))
            for line in csvreader:
                record = []
                if line[self.columns['ACCOUNT'][1]][:6] == '208100':
                    card_type = 'GCR'
                else:
                    card_type = 'CC'
                dept = line[self.columns['ACCOUNT'][1]][-2:]
                idate = datetime.strptime(line[self.columns['IDATE'][1]], "%m/%d/%Y")
                refno = line[self.columns['REFNO'][1]]
                amount = round(float(line[self.columns['AMOUNT'][1]]), 2)
                journal_type = line[self.columns['JOURNAL'][1]]
                if dept not in transactions:
                    transactions[dept] = {refno: [amount, idate, journal_type, card_type]}
                elif refno not in transactions[dept]:
                    transactions[dept][refno] = [amount, idate, journal_type, card_type]
                else:
                    transactions[dept][refno][0] += amount
        return transactions

    def ImportCHSData(self, filename):
        transactions = []
        with open(filename, 'r', encoding='utf-8-sig') as filename:
            c_reader = csv.reader(filename, dialect = "excel")
            skip_list = ['B', 'D', 'W', 'G', 'R', 'P']
            chs_dict = {}
            for line in c_reader:
                if not line[0] or line[0][0] in skip_list or line[0] == 'Transaction Detail':
                    continue
                elif line[0].replace(' ', '').strip(':') in self.merchant_ids.keys():
                    merch_id = line[0].replace(' ', '')
                elif line[0] in self.columns:
                    self.MapHeaderToColumns(line)
                else:
                    try:
                        in_out = line[self.columns['I/O'][1]]
                        idate = datetime.strptime(line[self.columns['Tran Date'][1]],
                                                  '%m/%d/%Y %I:%M:%S %p')
                        batch_date = datetime.strptime(line[self.columns['Batch Date'][1]],
                                                    '%m/%d/%Y')
                        card_type = line[self.columns['Card Type'][1]]
                        amount = self.ConvertAmount(line[self.columns['Tran Amount'][1]])
                        tran_type = line[self.columns['Tran Type'][1]]
                        auth_no = line[self.columns['Auth Code'][1]]
                        transactions.append([merch_id, idate, batch_date, card_type, amount, tran_type, auth_no, in_out])
                    except Exception as e:
                        print(str(e))
                        print(line)
        return transactions

def main():
    ap = ImportData()
    test_data_path = '/home/adam/projects/cc_rec/test_data'
    ap_trans = ap.ImportAPData(path.join(test_data_path, '121.csv'))
    chs_trans = ap.ImportCHSData(path.join(test_data_path, 'TransactionDetail.csv'))

if __name__ == '__main__':
    main()
