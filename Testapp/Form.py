from typing import Any, Dict
from django import forms
from django.core import validators
def GmailValidator(value):
    if value[len(value)-9:]!='gmail.com':
        raise forms.ValidationError('mail must be gamil ')
class StuInfo(forms.Form):
    UserName=forms.CharField(max_length=80,validators=[validators.MaxLengthValidator(10)])
    Age=forms.IntegerField(max_value=100)
    Address=forms.CharField(max_length=100)
    Email=forms.EmailField(validators=[GmailValidator])

    def clean(self):
        print('Total validation ')
        clean_data=super().clean()
        inputAge=clean_data['Age']
        if inputAge==20:
            raise forms.ValidationError('age must be greater than 20')
        












#explisit validation
#    def clean_UserName(self):
#        inputname=self.cleaned_data['UserName']
#        print('validating name')
#        if len(inputname)<4:
#            raise forms.ValidationError('length of the student must be greater than 4')
#
#    def clean_Age(self):
#        inputage=self.cleaned_data['Age']
#        print('validating Age')
#        if inputage<100 and inputage<20:
#            raise forms.ValidationError('The student age must between 20 and 100')
        

