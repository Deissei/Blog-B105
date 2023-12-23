from django.urls import path

from apps.comments.views import delete_comment, update_comment


urlpatterns = [
    path('delete_comment/<int:pk>', delete_comment, name='delete_comment'),
    path('update_comment/<int:pk>', update_comment, name='update_comment'),
]