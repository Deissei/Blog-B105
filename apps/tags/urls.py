from django.urls import path
from apps.tags.views import(
    index,
    detail_tag,
    delete_tag,
    update_tag,
)

urlpatterns = [
    path('tags/',index,name='tags'),
    path('detail_tag/<int:pk>',detail_tag,name='detail_tag'),
    path('delete_tag/<int:pk>',delete_tag,name= 'delete_tag'),
    path('update_tag/<int:pk>',update_tag,name='update_tag'),
]