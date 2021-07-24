from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import Post
from .forms import PostForm, RegistrationForm, SingInForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def sing_in(request):
    if request.method == "POST":
        form = SingInForm(request.POST)
        username=form['username'].data
        password=form['password'].data
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
    else:
        form = SingInForm()
    return render(request, "registration/login.html", {'form': form})

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return redirect('sing_in')
    else:
        form = RegistrationForm()
    return render(request, "registration/registration.html", {'form': form})

def sing_out(request):
    logout(request)
    return redirect('/')


def log_info(request):
    print('scheme:', request.scheme)
    print('body:', request.body)
    print('path:', request.path)
    print('path_info:', request.path_info)
    print('method:', request.method)
    print('encoding:', request.encoding)
    print('content_type:', request.content_type)
    print('content_params:', request.content_params)
    print('GET:', request.GET)
    print('POST:', request.POST)
    print('COOKIES:', request.COOKIES)
    print('FILES:', request.FILES)
#    print('META:', request.META)
    print('headers:', request.headers)
    print('user:', request.user)
    print('get_host:', request.get_host())
