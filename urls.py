from django.urls import path
from . import views  # Assuming this is where your view functions are defined

# Add this to your urlpatterns list

path('log-captcha', views.log_captcha, name='log_captcha'),
path('captcha-log/', views.captcha_log, name='captcha_log'),
