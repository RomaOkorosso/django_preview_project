from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.viewsets import ModelViewSet

from django_preview_project.post.models import Post, Comment, Like, Dislike
from django_preview_project.post.forms import PostForm, LikeForm, DislikeForm, CommentForm
from django_preview_project.post.serializers import PostSerializer, CommentSerializer, LikeSerializer, DislikeSerializer


class PostListViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeListViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DislikeListViewSet(ModelViewSet):
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = 'account_login'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    login_url = 'account_login'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    login_url = 'account_login'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    login_url = 'account_login'

