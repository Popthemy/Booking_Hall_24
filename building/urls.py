from django.urls import path
from . import views

urlpatterns = [
    path('', views.halls ,name='all-halls'),
    path('hall/<str:pk>/', views.single_hall ,name='single-hall'),
    path('create-hall/', views.createHall ,name='create-hall'),
    path('delete-hall/<str:pk>/', views.deleteHall ,name='delete-hall'),

]