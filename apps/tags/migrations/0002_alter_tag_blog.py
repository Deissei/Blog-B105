# Generated by Django 5.0 on 2023-12-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_user'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='blog',
            field=models.ManyToManyField(related_name='tags', to='blogs.blog', verbose_name='Блог'),
        ),
    ]