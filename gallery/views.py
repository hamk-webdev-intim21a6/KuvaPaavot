from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import UploadForm
from django.template import loader


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
            image_upload = form.save(commit=False)
            image_upload.author = request.user
            image_upload.save()
            return redirect('gallery:success')
    else:
        form = UploadForm()
    return render(request, 'gallery/upload.html', {'form' : form})

def success(request):
    #return render(request, 'gallery/success.html', {})
    template = loader.get_template('gallery/success.html')
    return HttpResponse(template.render())