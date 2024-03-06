from django.urls import path
from . import views


urlpatterns = [
  path('admin-add-rep/', views.admin_add_rep, name='admin-add-rep'),
  path('view-reps/', views.view_all_reps, name='all-reps'),
  path('edit-reps-details/<str:pk>/', views.edit_rep_details, name='edit-rep-details'),
  path('delete-reps-details/<str:pk>/', views.delete_rep_details, name='delete-rep-details'),

]
