from django.shortcuts import render, redirect
from models import Blog_Comment
from ..User.models import User
from django.contrib import messages
from django.db.models import Count
# Create your views here.
def index(request):
    context={
     "Blog":Blog_Comment.objects.all()
    }
    return render(request, 'python_exam/index.html', context)

def check(request):
    response = Blog_Comment.objects.check_Blog(request.POST)
    if not response['status']:
        for error in response['errors']:
            messages.error(request, error)
    return redirect('Blog:blog_and_comment')

def add_to(request,id):
    context={
     "blog":Blog_Comment.objects.get(id=id)
    }
    return redirect('Blog:index')

def blog_and_comment(request):
    return redirect('Blog:index')

def show_information(request,id):
    context={
     "blog":Blog_Comment.objects.get(id=id),
    }
    return render(request,'python_exam/show.html',context)
