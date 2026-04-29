from django.urls import path
from . import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('my-attendance/', views.student_attendance, name='student_attendance'),
]