from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True) 
      return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def login(request):
    pass