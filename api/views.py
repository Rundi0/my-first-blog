from django.contrib.auth.models import Group, User

from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView, 
    ListAPIView, 
    RetrieveUpdateDestroyAPIView, 
    ListCreateAPIView,
    get_object_or_404,
)
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, ViewSet

from blog.models import Comment, Post
from .serializers import (
    CommentCreateSerializer, 
    CommentSerializer, 
    GroupSerializer, 
    PostListSerializer, 
    PostDetailSerializer, 
    UserSerializer,
)

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializers = PostListSerializer(posts, many=True)
        return Response(serializers.data)


class PostDetailView(APIView):
    def get(self, request, pk):
        post = Post.objects.filter(id=pk)
        serializers = PostDetailSerializer(post, many=True)
        return Response(serializers.data)


class CommentView(APIView):
    def get(self, request, pk):
        comment = Comment.objects.filter(post=pk)
        serializers = CommentSerializer(comment, many=True)
        return Response(serializers.data)

    def post(self, request, pk):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
            return Response(status=201)
        return Response(status=400)


class UsersView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": True,
                         "message": "Organization Added !",
                         "data": serializer.data},
                        status=status.HTTP_201_CREATED, headers=headers)


class UsersDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": True,
                         "message": "Organization Added !",
                         "data": serializer.data},
                        status=status.HTTP_201_CREATED, headers=headers)


class GroupViewSet(ViewSet):
    def list(self, request):
        queryset = Group.objects.all()
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Group.objects.all()
        group = get_object_or_404(queryset, pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
