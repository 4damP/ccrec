from django import forms
from django.forms import ModelForm

from .models import UploadDocument #AccountsPlusImport, CHSImport

def upload_file(*args, **kwargs):
    if args:
        for arg in args:
            print(arg)

# @require_POST
def form_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'imports', request.FILES['file'])
    path = default_storage.save(save_path, request.FILES['file'])
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'rec/upload.html', {'form': form})

class DocumentForm(forms.Form):
    class Meta:
        model = UploadDocument
        fields = ('description', 'docfile')



#
# class APdataForm(forms.ModelForm):
#     class Meta:
#         model = AccountsPlusImport
#         fields = ('dept', 'refno', 'idate', 'amount',
#                   'journal_type', 'tran_type', 'auth_no',
#                   'card_type', 'reconciled', 'batch_date')
#
# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()
