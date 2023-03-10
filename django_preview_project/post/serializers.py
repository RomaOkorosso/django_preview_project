from django_preview_project.post.models import Post, Like, Dislike, Comment
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'content', 'date_posted', 'author', 'likes', 'dislikes', 'comments']


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ['url', 'post', 'author']


class DislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dislike
        fields = ['url', 'post', 'author']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'author', 'content', 'post']
