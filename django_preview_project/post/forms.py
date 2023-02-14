# forms for Post, Likes, Dislikes, Comments

from django import forms
from django_preview_project.post.models import Post, Like, Dislike, Comment
from django_preview_project.user.models import Profile


class PostForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ('title', 'content',)

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.author = Profile.objects.get(user=self.user)
        if commit:
            post.save()
        return post


class LikeForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.HiddenInput())
    post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Like
        fields = ('user', 'post',)

    def save(self, commit=True):
        like = super(LikeForm, self).save(commit=False)
        like.user = Profile.objects.get(user=self.user)
        like.post = Post.objects.get(id=self.post)
        if commit:
            like.save()
        return like


class DislikeForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.HiddenInput())
    post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Dislike
        fields = ('user', 'post',)

    def save(self, commit=True):
        dislike = super(DislikeForm, self).save(commit=False)
        dislike.user = Profile.objects.get(user=self.user)
        dislike.post = Post.objects.get(id=self.post)
        if commit:
            dislike.save()
        return dislike


class CommentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.HiddenInput())
    post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('user', 'post', 'content',)

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.user = Profile.objects.get(user=self.user)
        comment.post = Post.objects.get(id=self.post)
        if commit:
            comment.save()
        return comment
