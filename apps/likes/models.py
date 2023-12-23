from django.contrib.auth.models import User
from django.db import models


from apps.blogs.models import Blog


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_likes',
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='blog_likes',
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
