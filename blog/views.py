from mysite.celery import app
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.views import View
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

from blog.models import Comment, Post
from blog.forms import PostForm, SendMailForm, SingInForm, RegistrationForm, CommentForm, TaskForm
from blog.postmark import send_mail_simple
from .tasks import add, celery_send_mail
from mysite.celery import debug_task

class SendMailView(View):
    def get(self, request):
        form = SendMailForm()
        return render(request, 'registration/sand_email.html', {'form': form})

    def post(self, request):
        to_mail = request.POST['email']
        title = request.POST['title']
        text = request.POST['text']
        if not all((to_mail, title, text)):
            return HttpResponse("Incorrect data!")
        
        celery_send_mail.delay((to_mail,), title, text)

        return HttpResponse("Your mail send!")

class SendRegularTask(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'registration/sand_email.html', {'form': form})

    def post(self, request):
        text = request.POST['text']
        if not text:
            return HttpResponse("Incorrect data!")
        
        PeriodicTask.objects.create(
					name='Repeat order {}'.format(1),
					task='mysite.celery.test',
					interval=IntervalSchedule.objects.get(every=10, period='seconds'),
					args=json.dumps([text]),
					start_time=timezone.now(),
		)
        
        return HttpResponse("Your task send!")

class PostNew(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        return render(request, 'blog/post_edit.html', {'form': form})


class PostEdit(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        return render(request, 'blog/post_edit.html', {'form': form})

class SingIn(View):
    def get(self, request):
        form = SingInForm()
        return render(request, "registration/login.html", {'form': form})

    def post(self, request):
        form = SingInForm(request.POST)
        user = authenticate(username=form['username'].data, password=form['password'].data)
        if user is not None:
            login(request, user)
            return redirect('/')
        form = SingInForm()
        return render(request, "registration/login.html", {'form': form})

class Registration(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "registration/registration.html", {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return redirect('sing_in')
        return render(request, "registration/registration.html", {'form': form})

class PostDetalis(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=pk)
        comment_form = CommentForm()
        return render(request, 'blog/post_detail.html', 
            {'post': post, 'comments': comments, 'comment_form': comment_form})
  
    def post(self, request, pk):
        comment = Comment()
        comment.text = request.POST['text']
        comment.post_id = pk
        comment.author_id = request.user.id
        comment.save()
        return self.get(request, pk)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def sing_out(request):
    logout(request)
    return redirect('/')


def my_posts(request):
    posts = Post.objects.filter(author=User.objects.get(username=request.user).id)
    return render(request, "blog/post_list.html", {'posts':posts})


def profile_user(request):
    return render(request, "")


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
    print('META:', request.META)
    print('headers:', request.headers)
    print('user:', request.user)
    print('get_host:', request.get_host())
 