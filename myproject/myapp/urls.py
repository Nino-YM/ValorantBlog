from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('teams/', views.teams_view, name='teams'),
    path('tournaments/', views.tournaments_view, name='tournaments'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<int:pk>/', views.edit_article, name='edit_article'),
]
