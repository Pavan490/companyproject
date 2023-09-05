from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from.models import *
from.serializers import*
@api_view(['GET'])
def demo(request):
    student_data=Student.objects.all()
    serializer=StudentSerializer(student_data,many=True)
        
    return Response({'status':200,
                     'payload':serializer.data})
    
@api_view(['POST'])
def post_student(request):
    data=request.data
    print(data)
    return Response({'status':300,
                     'payload':data})