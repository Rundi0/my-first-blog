import django
from django.urls import path
from django.contrib import auth
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sing_in/', views.sing_in, name='sing_in'),
    path('sing_out/', views.sing_out, name='sing_out'),
    path('registration/', views.registration, name='registration'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/my_posts', views.my_posts, name='my_posts'),
]