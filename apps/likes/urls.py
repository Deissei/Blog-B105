from django.urls import path

from apps.likes.views import add_like,add_like_comment

urlpatterns = [
    path('add_like/<int:pk>', add_like, name='add_like'),
    path('add_like_comment/<int:pk>', add_like_comment, name='add_like_comment'),
]