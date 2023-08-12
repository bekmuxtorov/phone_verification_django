from django.urls import path
from . import views


urlpatterns = [
    path('sent_code/', views.sent_verification_code),
    path('verify_code/', views.verify_code)
]
