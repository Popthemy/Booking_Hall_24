from django.urls import path
from . import views

urlpatterns = [
    path('halls/', views.halls ,name='all-halls'),
    path('hall/<str:pk>/', views.single_hall ,name='single-hall'),
]
