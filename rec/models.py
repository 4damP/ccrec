from django.db import models
# from ImportCHSData import ImportCHSData
#
# class MyCsvModel(model):
#     pass


class Dept(models.Model):
    dept_no = models.CharField(max_length=2, unique=True)
    dept_base = models.CharField(max_length=2)
    dept_description = models.CharField(max_length=30)
    merchant_id = models.CharField(max_length=10)
    tran_type = models.CharField(max_length=1)

    def __str__(self):
        # return dept_description
        pass

    def all_depts_dict(self):
        pass


class Transactions(models.Model):
    # dept = models.ForeignKey(Depts)
    dept = models.PositiveSmallIntegerField()
    refno = models.PositiveSmallIntegerField()
    idate = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    journal_type = models.CharField(max_length=20)
    tran_type = models.CharField(max_length=2)
    auth_no = models.CharField(max_length=20)
    card_type = models.CharField(max_length=10)
    reconciled = models.BooleanField()
    batch_date = models.DateField()

    def __str__(self):
        return f'{dept}, {refno}, {idate}, {amount}, {journal_type},\
                 {tran_type}, {auth_no}, {card_type}, {reconciled}, {batch_date}'

class Payments(models.Model):
    dept = models.PositiveSmallIntegerField()
    refno = models.PositiveSmallIntegerField()
    idate = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    journal_type = models.CharField(max_length=20)
    tran_type = models.CharField(max_length=2)
    auth_no = models.CharField(max_length=20)
    card_type = models.CharField(max_length=10)
    reconciled = models.BooleanField()
    batch_date = models.DateField()

    def __str__(self):
        return f'{dept}, {refno}, {idate}, {amount}, {journal_type},\
                 {tran_type}, {auth_no}, {card_type}, {reconciled}, {batch_date}'

class Progress(models.Model):
    period = models.DateField()
    import_ap = models.BooleanField(default=False)
    import_chs = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    gl_balance = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return [self.period, self.import_ap, self.import_chs, self.closed, self.gl_balance]

class UploadDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)
    docfile = models.FileField(upload_to='imports')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('/')
