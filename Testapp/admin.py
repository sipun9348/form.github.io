from django.contrib import admin
from Testapp.models import StudentInfo
# Register your models here.
class Liso(admin.ModelAdmin):
    lis=["name","age","address"]
admin.site.register(StudentInfo,Liso)

