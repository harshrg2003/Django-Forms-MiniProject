from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from myapp.models import Post
from myapp.forms import UploadForm
# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,"index.html",{'posts':posts})

def create_post(request):
    if request.method=="POST":
        form=UploadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home') 
    return render(request,"Forms.html",{"form":UploadForm})   
