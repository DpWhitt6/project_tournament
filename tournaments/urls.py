from django.urls import path
from . import views

urlpatterns = [
    path('', views.tournament_list, name='tournament_list'),
    path('tournament/<int:pk>/', views.tournament_detail, name='tournament_detail'),
    path('tournament/create/', views.create_tournament, name='create_tournament'),
    path('tournament/<int:pk>/register/team/', views.register_team, name='register_team'),
    path('tournament/<int:pk>/register/individual/', views.register_individual, name='register_individual'),
]