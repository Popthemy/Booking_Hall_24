from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.create_rep, name='register-rep' ),
    path('login/', views.login_rep, name='login-rep' ),
    path('logout/', views.logout_rep, name='logout-rep' ),
    path('edit-rep-profile/', views.edit_rep_profile, name='edit-rep-profile' ),
    path('dashboard/', views.rep_dashboard, name='dashboard' ),
]
