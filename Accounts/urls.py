from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('login/', views.LoginUser.as_view()),
    path('createuser/', views.CreateUser.as_view()),
    path('activeaccount/<str:code>',views.ActiveAccount)

]