from django import forms
import datetime
# from .models import UploadDocument, Progress

class UploadFileForm(forms.Form):
    month = forms.ChoiceField(choices=[(x, x) for x in range(1, 13)])
    yyyy = datetime.date.today().year
    year = forms.ChoiceField(choices=[(x, x) for x in range(yyyy-1, yyyy+2)])
    file_choices = (('credit', 'Credit'), ('gift_card', 'Gift'), ('payment', 'Payment'))
    file_type = forms.ChoiceField(choices=file_choices)
    # type = forms.CharField(max_length=50)
    file = forms.FileField()

    def clean_file_type(self):
        data = self.cleaned_data['file_type']
        if data[-3:] == '.csv':
            raise ValidationError(_('Invalid file type, expecting a comma separated value (.csv) file.'))
        return data

    def get_file_type(self):
        return file_type
