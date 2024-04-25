from django.urls import path
from .views import views

urlpatterns = [
    path("", views.home, name="home"),
    path('users', views.create_user, name='create_user'),
    path('users/<int:userid>', views.update_user, name='update_user'),
    path('users/sign-in', views.user_sign_in, name='user_sign_in'),
    path('refresh-token', views.refresh_token, name='refresh_token'),
    path('users', views.get_users, name='get_users'),
    path('users/statistics', views.get_all_users_statistics, name='get_all_users_statistics'),
    path('users/<int:userid>/statistics', views.get_user_statistics, name='get_user_statistics'),
]