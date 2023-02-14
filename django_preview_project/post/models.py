from django.db import models

from django_preview_project import user


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    likes = models.ManyToManyField('Like', related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField('Dislike', related_name='post_dislikes', blank=True)
    comments = models.ManyToManyField('Comment', related_name='post_comments', blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def total_comments(self):
        return self.comments.count()

    def add_like(self, user):
        like = Like.objects.create(user=user)
        self.likes.add(like)
        self.save()

    def add_dislike(self, user):
        dislike = Dislike.objects.create(user=user)
        self.dislikes.add(dislike)
        self.save()

    def add_comment(self, user, content):
        comment = Comment.objects.create(user=user, content=content)
        self.comments.add(comment)
        self.save()

    def remove_like(self, user):
        like = Like.objects.get(user=user)
        self.likes.remove(like)
        self.save()

    def remove_dislike(self, user):
        dislike = Dislike.objects.get(user=user)
        self.dislikes.remove(dislike)
        self.save()

    def remove_comment(self, user, content):
        comment = Comment.objects.get(user=user, content=content)
        self.comments.remove(comment)
        self.save()

    def get_comments(self):
        return self.comments.all()

    def get_likes(self):
        return self.likes.all()

    def get_dislikes(self):
        return self.dislikes.all()

    def get_author(self):
        return self.author.user.username

    def get_author_profile(self):
        return self.author


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username


class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username
