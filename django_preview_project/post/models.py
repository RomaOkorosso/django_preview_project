from django.db import models
from django.core.exceptions import BadRequest
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
        return self.author.username

    def get_author_profile(self):
        return self.author


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        db_like = Like.objects.filter(author=self.author)
        if db_like:
            raise BadRequest('User already liked this post')
        super().save(force_insert, force_update, using, update_fields)


class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        db_dislike = Like.objects.filter(author=self.author)
        if db_dislike:
            raise BadRequest('User already disliked this post')
        super().save(force_insert, force_update, using, update_fields)
