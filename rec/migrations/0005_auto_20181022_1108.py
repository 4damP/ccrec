# Generated by Django 2.1.2 on 2018-10-22 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0004_document'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='UploadDocument',
        ),
        migrations.RenameField(
            model_name='uploaddocument',
            old_name='document',
            new_name='docfile',
        ),
    ]
