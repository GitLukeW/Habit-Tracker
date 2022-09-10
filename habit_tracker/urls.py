from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_habits, name='daily_habits'),
    path('habit/<int:pk>', views.habit_detail, name='habit_detail'),
    path('habit/new/', views.habit_new, name='habit_new'),
    path('habit/<int:pk>/edit/', views.habit_edit, name='habit_edit'),
    path('habit/<pk>/remove/', views.habit_remove, name='habit_remove'),
]   
