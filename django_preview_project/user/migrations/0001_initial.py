# Generated by Django 4.1.7 on 2023-02-14 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('comments', models.ManyToManyField(blank=True, to='post.comment')),
                ('dislikes', models.ManyToManyField(blank=True, to='post.dislike')),
                ('likes', models.ManyToManyField(blank=True, to='post.like')),
                ('posts', models.ManyToManyField(blank=True, to='post.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
