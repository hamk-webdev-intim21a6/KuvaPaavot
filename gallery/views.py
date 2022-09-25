from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import UploadForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the gallery index.")

def display_images(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'gallery/index.html', {'posts' : posts})

def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:success')
    else:
        form = UploadForm()
    return render(request, 'gallery/upload.html', {'form' : form})


def success(request):
    return render(request, 'gallery/success.html', {})