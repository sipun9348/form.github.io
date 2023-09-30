from django.shortcuts import render
from Testapp.models import StudentInfo
from .Form import StuInfo
# Create your views here.
def Temp(req):
    s=StudentInfo.objects.all()
    my_dick={'student':s}
    return render(req,'Hello.html',context=my_dick) 
def RegForm(req):
    frm=StuInfo()
    if req.method=='POST':
        frm=StuInfo(req.POST)
        if frm.is_valid():
            print('name of the student is ',frm.cleaned_data['UserName'])
            print('Age of the student is ',frm.cleaned_data['Age'])
            print('Address of the student is ',frm.cleaned_data['Address'])
            print('E-mail of the student is ',frm.cleaned_data['Email'])
    return render(req,'Register.html',{'form':frm})