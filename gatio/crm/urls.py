from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_next_batch/', views.get_next_batch, name='get_next_batch'),
    path('accounts/login/', auth_views.LoginView.as_view(), name ='login'),

]
