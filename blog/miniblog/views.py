from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post,contact
# Create your views here.
#Home
def home(request):
    posts = Post.objects.all()
    return render(request,'miniblog/home.html',{'post':posts})

#about
def about(request):
    return render(request,'miniblog/about.html')

#contact
def Contact(request):
    if request.method=="POST":
        nm = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        desc = request.POST['desc']
        con = contact(name=nm, email=email, address=address, desc=desc)
        con.save()
        return redirect('/contact/')
    else:
        return render(request,'miniblog/contact.html')

#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        posts = Post.objects.filter(uname = username)
        return render(request,'miniblog/dashboard.html',{'post':posts})
    else:
        return redirect('/login/')
#logout
def user_logout(request):
    logout(request)
    return redirect('/')

#signup
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation id created!!!')
            form.save()
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request,'miniblog/signup.html',{'form':form})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pw = form.cleaned_data['password']
                user = authenticate(username=uname,password=pw)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in sucessfully!!!!!!!")
                    return redirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'miniblog/login.html',{'form':form})
    else:
       return redirect('/dashboard/')

#Add new Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                uname = request.user.username
                pst = Post(title=title,desc=desc,uname = uname)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'miniblog/addpost.html',{'form':form})
    else:
        return redirect('/login/')

#Update Post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                form =PostForm()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'miniblog/updatepost.html',{'form':form})
    else:
        return redirect('/login/')
#Delete Post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return redirect('/dashboard/')
    else:
        return redirect('/login/')

