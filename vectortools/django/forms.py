from django.forms import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()
