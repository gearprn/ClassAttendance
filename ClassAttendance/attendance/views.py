from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course(request):
    return HttpResponse("All course that available")

def course_detail(request, course_id):
    return HttpResponse("Course %d syllabus" %course_id)

def course_qr(request, course_id):
    return HttpResponse("Course %d QR-code" %course_id)