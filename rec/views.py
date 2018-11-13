import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.views.generic import CreateView, FormView
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage

from .models import Dept, Progress, Transactions, Payments, UploadDocument
from .forms import UploadFileForm

def handle_uploaded_file(f, file_type):
    filename = f'{file_type}.csv'
    save_file = os.path.join('media/imports', filename)
    with open(save_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = f"{form.cleaned_data['year']}_{form.cleaned_data['month']}_{form.cleaned_data['file_type']}.csv"
            handle_uploaded_file(request.FILES['file'], filename)
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'rec/upload_file.html', {'form': form} )


class UploadDocument(CreateView):
    model = UploadDocument
    fields = ('period', 'type', 'docfile')
    template_name = 'rec/upload_file.html'
    context_object_name = 'upload_progress_list'
    # success_url = reverse('progress')
    # def get_queryset(self):
    #     return UploadDocument.objects.all()

class AddDept(CreateView):
    model = Dept
    fields = ('dept_no', 'dept_base', 'dept_description', 'merchant_id', 'tran_type')

class IndexView(generic.ListView):
    template_name = 'rec/index.html'
    context_object_name = 'progress_info_list'
    def get_queryset(self):
        progress = Progress.objects.order_by('-period')[:5]
        for each in progress:
            print(each)
        return progress

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['dept_info_list'] = Dept.objects.order_by('dept_no')
        return context

    def get_form_template(self, *args, **kwargs):
        form = super(UploadFileForm, self).get_context_data(*args, **kwargs)
        context_object_name = 'upload_form'
        return form

    def handle_uploaded_file(f, file_type):
        filename = f'{file_type}.csv'
        save_file = os.path.join('media/imports', filename)
        with open(save_file, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def upload_file(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                filename = f"{form.cleaned_data['year']}_{form.cleaned_data['month']}_{form.cleaned_data['file_type']}.csv"
                self.handle_uploaded_file(request.FILES['file'], filename)
                return HttpResponseRedirect('/')
        else:
            form = UploadFileForm()
        return render(request, 'rec/upload_file.html', {'form': form} )

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
