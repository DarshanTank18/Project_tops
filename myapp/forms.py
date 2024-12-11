from django import forms
from .models import *

class signupform(forms.ModelForm):
    class Meta:
        model = signuptbl
        fields = '__all__'

class updateform(forms.ModelForm):
    class Meta:
        model = signuptbl
        fields = ['id','fnm','email','number','password']

class notesForm(forms.ModelForm):
    class Meta:
        model=nodetbl
        fields='__all__'

class contectForm(forms.ModelForm):
    class Meta:
        model=contectustbl
        fields='__all__'