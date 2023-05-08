from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.student_create_view, name='student_add'),
    path('<int:pk>/', views.student_update_view, name='student_change'),


    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
]