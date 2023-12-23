from django.db import models

from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    title = models.CharField(
        max_length=123,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="blogs/",
        verbose_name="Фото",
    )

    def get_count_like(self):
        return sum([like.count for like in self.blog_likes.all()])

    def __str__(self):
        return f"{self.title}"
    

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
