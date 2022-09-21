from django.urls import path
from .views import student_details

urlpatterns = [
    path('',student_details.as_view())
]