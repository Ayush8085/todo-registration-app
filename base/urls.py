from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('edit/<str:pk>/', views.editTask, name='edit'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
