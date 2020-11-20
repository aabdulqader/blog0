from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm, AddPostForm
from django.contrib import messages
from .models import Post, Contact
from django.contrib.auth.models import Group


def postdetail(request, id):
    post = Post.objects.get(pk=id)

    context = {
        'post':post
    }
    return render (request, 'home/postdetails.html',context)





def home(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Post(title=title, desc=desc)
                post.save()
                form = AddPostForm()

        else:
            form = AddPostForm()
    else:
        if request.method == 'POST':
            form = LoginForm(request=request, data= request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully!")
                    return redirect('home')
        else:
            form = LoginForm()

    context = {
        'posts':posts,
        'form':form
    }
    return render (request, 'home/index.html', context)

def about(request):
    return render (request, 'home/about.html')

def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ins = Contact(name=name, email=email, subject=subject,message=message)
        ins.save()
    return render (request, 'home/contact.html')


def addpost(request):
    if request.user.is_authenticated:
        new_post = Post.objects.all()
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Post(title=title, desc=desc)
                post.save()
                form = AddPostForm()

        else:
            form = AddPostForm()
            
        context = {
        'form':form,
        'new_post':new_post
        }

        return render (request, 'home/addpost.html', context)
    else:
        return redirect ('login')


def updatepost(request, id):
    if request.user.is_authenticated:
        new_post = Post.objects.all()
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Post(title=title, desc=desc)
                post.save()
                form = AddPostForm()

        else:
            form = AddPostForm()
            
        context = {
        'form':form,
        'new_post':new_post
        }

        return render (request, 'home/update.html', context)
    else:
        return redirect ('login')

def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return redirect ('dashboard')
    else:
        return redirect ('login')



def dashboard(request):
    posts = Post.objects.all()

    user = request.user
    full_name = user.get_full_name()
    groups = user.groups.all()



    context = {
        'posts':posts,
        'full_name':full_name,
        'groups':groups
    }
    if  request.user.is_authenticated:
        return render (request, 'home/dashboard.html', context)
    else:
        return redirect('login')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            messages.success(request, "Congratulations! Your account has been created successfully.")
            return redirect ('login')
    else:
        form = SignUpForm()


    context = {
        'form':form
    }
            
    return render (request, 'home/signup.html', context)


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data= request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully!")
                    return redirect('dashboard')
        else:
            form = LoginForm()
        
        context = {
        'form':form
        }

        return render (request, 'home/login.html', context)
    else:
        return redirect ('dashboard')

def user_logout(request):
    logout(request)
    return redirect('home')
