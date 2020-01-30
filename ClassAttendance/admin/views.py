from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_student(request):
    return HttpResponse("Show all student")

def add_student(request):
    return HttpResponse('Add new student')

def edit_student(request, student_id):
    return HttpResponse('Edit student id: %d' % student_id)

def all_course(request):
    return HttpResponse('Show all course')

def add_course(request):
    return HttpResponse('Add new course')

def edit_course(request, course_id):
    return HttpResponse('Edit course id: %d' % course_id)