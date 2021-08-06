from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sing_in/', views.SingIn.as_view(), name='sing_in'),
    path('sing_out/', views.sing_out, name='sing_out'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('users/<int:pk>/', views.profile_user, name='profile_user'),
    path('post/<int:pk>/', views.PostDetalis.as_view(), name='post_detail'),
    path('post/new/', views.PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('post/my_posts/', views.my_posts, name='my_posts'),
    path('sand_email/', views.SendMailView.as_view(), name='sand_email'),
]