from django import forms 
from myapp.models import Post 

class UploadForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content','author']