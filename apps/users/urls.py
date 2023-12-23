from django.urls import path

from apps.users.views import signup_logics, login_logics, logout_logics


urlpatterns = [
    path('login/', login_logics, name='login'),
    path('sign_up/', signup_logics, name='sign_up'),
    path('logout/', logout_logics, name='logout'),
]