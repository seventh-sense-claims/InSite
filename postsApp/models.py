from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    post_image = models.ImageField(
        upload_to='postsApp/posts', blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='postsApp/videos',
                             default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
