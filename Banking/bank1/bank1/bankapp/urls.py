from django.urls import path
from . import views


app_name='bankapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('newpage/', views.newpage, name='newpage'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout_view, name='logout'),



    path('ajax/load-branch/', views.load_branch, name='ajax_load_branch'),
]