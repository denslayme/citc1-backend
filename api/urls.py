from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.user_login),

    # Procedures
    path('procedures/', views.get_procedures),
    path('procedures/<int:pk>/update/', views.update_procedure),
    path('procedures/<int:pk>/delete/', views.delete_procedure),

    # FAQs
    path('faqs/', views.get_faqs),
    path('faqs/<int:pk>/update/', views.update_faq),
    path('faqs/<int:pk>/delete/', views.delete_faq),

    # Requests
    path('requests/submit/', views.submit_request),
    path('requests/track/', views.track_requests),

    # Update & Delete
    path('procedures/<int:pk>/update/', views.update_procedure),
    path('procedures/<int:pk>/delete/', views.delete_procedure),
]