from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_view, name='login-view'),
  # path('login-route/', views.login_route, name='login-route'),
  path('logout/', views.logout, name='logout-view'),
  path('forgot-password/', views.forgot_password_view, name='forgot-password-view'),
  path('reset-password/', views.reset_password_view, name='reset-password-view'),
]