import csv
from os import path
from datetime import date
# from .models import Dept

class ImportAPdata():
    def __init__(self):
        # configuration dictionaries to be stored in an xml file
        self.columns = self.GetColumnReference()

    def GetDeptsDict(self):
        try:
            depts = Dept.objects.order_by('dept_no')
            for each in depts:
                print(each)
            return
        except Exception as e:
            print(str(e))

    def GetColumnReference(self):
        '''
        Map header columns based on config file.

        '''
        columns = {}
        with open('config.txt', 'r') as config:
            for line in config:
                line = line.split()
                columns[line[0]] = [line[2], 0]
        return columns

    def MapHeaderToColumns(self, header):
        for col in header:
            if col in self.columns:
                try:
                    self.columns[col][1] = header.index(col)
                except Exception as e:
                    print(str(e))

    def ConvertDate(self, idate):
        idate = [int(i) for i in idate.split('/')]
        return date(idate[2], idate[0], idate[1])

    def ImportData(self, filename):
        with open(filename, 'r', encoding='utf-8-sig') as filename:
            csvreader = csv.reader(filename)
            self.MapHeaderToColumns(next(csvreader, None))
            for line in csvreader:
                dept = line[self.columns['ACCOUNT'][1]][-2:]
                idate = self.ConvertDate(line[self.columns['IDATE'][1]])





class ImportCHSdata(object):
    pass

def main():
    ap = ImportAPdata()
    test_data_path = '/home/adam/projects/cc_rec/test_data'
    ap.ImportData(path.join(test_data_path, '121.csv'))

if __name__ == '__main__':
    main()
