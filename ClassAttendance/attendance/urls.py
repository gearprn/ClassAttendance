from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course, name='course'),
    path('course/<int:course_id>', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/qrcode', views.course_qr, name='course_qr')
]