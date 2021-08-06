from django.db import router
from django.urls import path
from django.contrib import auth
from rest_framework import viewsets
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'groups', views.GroupViewSet, basename='group')
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('posts/<int:pk>/comment', views.CommentView.as_view()),

    path('users/', views.UsersView.as_view(), name='user-list'),
    path('users/<int:pk>', views.UsersDetailView.as_view(), name='user-datail'),
    #path('comment/', views.CommentCreateView.as_view()),
]

urlpatterns += router.urls