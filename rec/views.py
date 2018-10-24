from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.views.generic import CreateView
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage

from .models import Dept, Progress, Transactions, Payments, UploadDocument
# from .forms import DocumentForm
# from .import_data import ImportAPdata

def UploadFile(*args, **kwargs):
    if args:
        for arg in args:
            print(arg)

@require_POST
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


class UploadDocumentView(CreateView):
    model = UploadDocument
    fields = ('description', 'docfile')



class AddDept(CreateView):
    model = Dept
    fields = ('dept_no', 'dept_base', 'dept_description', 'merchant_id', 'tran_type')


class Upload(generic.ListView):
    template_name = 'rec/upload.html'
    context_object_name = 'upload_file_list'
    def get_queryset(self):
        files = UploadDocument.objects.order_by('dept_no')
        return files


class IndexView(generic.ListView):
    template_name = 'rec/index.html'
    context_object_name = 'progress_info_list'
    def get_queryset(self):
        progress = Progress.objects.order_by('period')
        return progress

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['dept_info_list'] = Dept.objects.order_by('dept_no')
        return context
    #
    # def get_apdata_import(self, *args, **kwargs):
    #     form = PostForm()
    #     return render(request, 'rec/import_ap.html', {'form': form})
    #
    # def simple_upload(request):
    #     if request.method == 'POST' and request.FILES['myfile']:
    #         myfile = request.FILES['myfile']
    #         fs =FileSystemStorage()
    #         filename = fs.save(myfile.name, myfile)
    #         uploaded_file_url = fs.url(filename)
    #         return render(request, 'core/simple_upload.html', {
    #             'uploaded_file_url': uploaded_file_url
    #         })
    #     return render(request, 'core/simple_upload.html')

# class AP_Import(generic.FormView):
#     def get_queryset(self):
#         template_name = 'rec/apimport.html'
#         context_object_name = 'ap_import_form'
#         return render(request, 'rec/upload.html', {'form': form})

# class FileUpload(generic.ListView):
#     template_name = 'upload.html'
#     model = UploadDocument
#     fields = ['description', 'document']
#     def get_queryset(self):
#         form = UploadDocument.objects.order_by('id')
#         return render('request', 'rec/upload.html')

class DeptView(generic.ListView):
    template_name = 'rec/depts.html'
    context_object_name = 'dept_info_list'
    def get_queryset(self):
        depts = Dept.objects.order_by('dept_no')
        return depts

class ReconcileView(generic.ListView):
    template_name = 'rec/reconcile.html'
    context_object_name = 'rec_table'
    def get_queryset(self):
        ap_transactions = Transactions.objects.order_by('idate')
        chs_transactions = Payments.objects.order_by('idate')
        return [ap_transactions, chs_transactions]

class ProgressView(generic.ListView):
    template_name = 'rec/progress.html'
    context_object_name = 'progress_info_list'
    def get_queryset(self):
        progress = Progress.objects.order_by('period')
        return progress
