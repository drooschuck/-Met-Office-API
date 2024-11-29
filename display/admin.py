from django.contrib import admin
from .models import whole_city
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(whole_city)
class cityResource(ImportExportModelAdmin):
    pass