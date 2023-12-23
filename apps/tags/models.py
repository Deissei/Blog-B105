from django.db import models

from apps.blogs.models import Blog


class Tag(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Название',
    )
    blog = models.ManyToManyField(
        Blog,
        verbose_name='Блог',
        related_name='tags',
    )

    def __str__(self):
        return f'{self.title}'
    
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги' 