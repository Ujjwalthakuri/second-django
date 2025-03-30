from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
# Create your views here.

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response (serializer.data)
           
    elif request.method =="POST":
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data)
    
@api_view(['GET', 'DELETE'])
def Category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'GET' :
        serializer = CategorySerializer(category)
        return Response (serializer.data)
    elif request.method == 'DELETE':
        # order_item = order_item.objects.filter(Food__Category = category).count()
        # if order_item>0:
        #     raise ValidationError({'details': 'CANNOT DELETE'})
        category.delete()
        return Response({"detail": "Data deleted"}, status= status.HTTP_204_No_CONTENT)
        