from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.create_rep, name='register-rep'),
    path('login/', views.login_rep, name='login-rep'),
    path('logout/', views.logout_rep, name='logout-rep'),
    path('change_password/', views.rep_change_password,
         name='rep_change_password'),
    path('edit_rep_profile/', views.edit_rep_profile, name='edit-rep-profile'),
    path('dashboard/', views.rep_dashboard, name='dashboard'),



    # PATH FOR PASSWORD RESET
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset_view'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
]
