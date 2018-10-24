import csv

from .models import Dept

class ImportAPdata():
    def __init__(self):
        # configuration dictionaries to be stored in an xml file
        # self.depts = self.GetDeptsDict()
        pass

    def GetDeptsDict(self):
        try:
            depts = Dept.objects.order_by('dept_no')
            for each in depts:
                print(each)
            return
        except Exception as e:
            print(str(e))

    def GetColumnReference(line):
        '''
        Map header columns based on config file.

        '''
        self.columns = {}
        with open('config.txt', 'r'):
            self.columns[]



class ImportCHSdata(object):
    pass
