from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.all_student, name='student'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('course/', views.all_course, name='course'),
    path('add_course/', views.add_course, name='add_course'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course')
]