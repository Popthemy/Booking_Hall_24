from django.urls import path
from . import views

urlpatterns = [
    path( 'pre-schedule/<str:pk>/', views.create_preSchedule, name='pre-schedule'),
    path('main-schdule/<str:pk>/', views.create_mainSchedule, name='main-schedule')

]