from django.contrib import admin

from .models import Dept, Progress, UploadDocument

admin.site.register(Dept)
admin.site.register(Progress)
admin.site.register(UploadDocument)
