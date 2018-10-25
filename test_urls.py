from datetime import datetime

from rec.models import Transactions, Payments

# import rec.urls

# def test_urls(admin_client):
#     for each in ['', 'rec', 'home', 'depts', 'reconcile', 'progress', 'addDept']:
#         url = f'127.0.0.1:8000/{each}'
#         print(url)
#         response = admin_client.get(url, follow=True)
#         assert response.status_code == 200


class TransactionTestCase():
    def setup(self):
        inv_date = datetime.date('2018', '9', '1')
        Transactions.objects.create(dept='10', refno='123456', idate=inv_date,
                                    amount=25.00, journal_type='SA',
                                    tran_type='I', reconciled=False)
        # Payments.objects.create(dept='10', refno='123456', idate=inv_date,
        #                             amount=25.00, journal_type='SA',
        #                             tran_type='I', reconciled=False)

    def test_reconcile(self):
        trans = Transactions.objects.all()
        # payment = Payments.objects.all()
        self.assertEqual(trans.dept, '10')


def main():
    transactions = TransactionTestCase()
    transactions.test_reconcile()

if __name__ == "__main__":
    main()
