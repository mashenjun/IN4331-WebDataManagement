__author__ = 'mashenjun'
# In forms.py...
from django import forms

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()
    # print ("###################")
    # print(file)
    # print ("###################")
