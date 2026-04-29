from django.urls import path
from . import views

urlpatterns = [
    path('my-students/', views.teacher_students, name='teacher_students'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]