from django.urls import path
from . import views

urlpatterns = [
    path( 'pre-schedule/<str:pk>/', views.preSchedule, name='pre-schedule'),
    path('main-schdule/<str:pk>/', views.mainSchedule, name='main-schedule')

]

