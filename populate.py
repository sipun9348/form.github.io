import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','formproject3.settings')
import django
django.setup()
from Testapp.models import StudentInfo
from random import randint
from faker import Faker
fake=Faker()
def Age():
    num=randint(20,100)
    return int(num)
def Papu(n):
    for i in range(n):
        fname=fake.name()
        fage=Age()
        faddress=fake.address()
        femail=fake.email()
        kemo=StudentInfo.objects.get_or_create(name=fname,age=fage,address=faddress,email=femail)
Papu(25)