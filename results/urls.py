from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:student_id>/', views.add_result, name='add_result'),
    path('my-results/', views.student_results, name='student_results'),
]