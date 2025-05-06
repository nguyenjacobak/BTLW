# Add this to your urlpatterns

from django.urls import path
from . import views

# Add this line to your existing urlpatterns list:
path('captcha-log/', views.captcha_log, name='captcha_log'),
