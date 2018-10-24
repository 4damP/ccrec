from rec.import_data import ImportAPdata

def test_depts():
    ap = ImportAPdata()
    dept_no_list = ['10', '12', '20', '22']
    for each in dept_no_list:
        assertEqual(each, each.dept_no)
