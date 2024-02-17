from django.urls import path
from . import views

urlpatterns = [
    path( 'pre-schedule/<str:pk>/', views.create_preSchedule, name='pre-schedule'),
    path('main-schedule/<str:pk>/', views.create_mainSchedule, name='main-schedule'),
    path('edit-preschedule/<str:pk>/', views.editPreSchedule, name='edit-preschedule'),
    path('edit-mainschedule/<str:pk>/', views.editMainSchedule, name='edit-mainschedule'),

]