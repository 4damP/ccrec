from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.urls import re_path

from . import views, forms

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rec', views.IndexView.as_view(), name='rec'),
    path('home', views.IndexView.as_view(), name='home'),
    path('depts', views.DeptView.as_view(), name='depts'),
    path('reconcile', views.ReconcileView.as_view(), name='reconcile'),
    path('progress', views.ProgressView.as_view(), name='progress'),
    path('addDept', views.AddDept.as_view(), name='addDept'),
    # path('upload', forms.upload_file(), name='UploadFile'),
    # path('apimport', views.AP_Import.as_view(), name='ap_import'),
    # path('upload', views.FileUpload.as_view(), name='upload'),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
