from django.shortcuts import render, redirect

from apps.likes.models import Like
from apps.blogs.models import Blog
from apps.comments.models import Comment,LikeForComment



def add_like(request, pk):
    blog = Blog.objects.get(id=pk)

    try:
        like = Like.objects.get(
            user=request.user,
            blog=blog
        )
        like.delete()
    except Like.DoesNotExist:
        like = Like.objects.create(
            user=request.user,
            blog=blog,
        )

    return redirect('detail_blog', pk=blog.id)

def add_like_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    try:
        like = LikeForComment.objects.get(
            user=request.user,
            comment=comment,
        )
        like.delete()
    except LikeForComment.DoesNotExist:
        like = LikeForComment.objects.create(
            user=request.user,
            comment=comment,
        )
    return redirect('detail_blog', pk=comment.blog.id)


