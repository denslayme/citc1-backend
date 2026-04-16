from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.user_login),
    path('procedures/', views.get_procedures),
    path('faqs/', views.get_faqs),
    path('requests/submit/', views.submit_request),
    path('requests/track/', views.track_requests),
]