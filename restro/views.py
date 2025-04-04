from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework.views import APIView
# from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView,ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView,  RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CataegorySerializer
    # def list(self, request):
    #     category = Category.objects.all()
    #     serializer = CategorySerializer(category, many=True)
    #     return Response (serializer.data)
    
    # def create(self, request):
    #     serializer = CategorySerializer(data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response (serializer.data)
        

# class categoryAPIView(ListAPIView, CreateAPIView):
class categoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CataegorySerializer
    
    # def get(self, request):
    #     category = Category.objects.all()  
    #     serializer = CategorySerializer(category, many=True)
    #     return Response (serializer.data)

    # def post(self, request):
    #     serializer = CategorySerializer(data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response (serializer.data)
         
# class Category_detailAPIVIEW(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
class Category_detailAPIVIEW(RetrieveUpdateDestroyAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CataegorySerializer
    
    # def get (self, request, pk):
    #     category = Category.objects.get(pk=pk)
    #     serializer = CategorySerializer(category)
    #     return Response (serializer.data)

    # def put(self, request, pk):
    #     category = Category.objects.get(pk=pk)
    #     serializer = CategorySerializer(category, data= request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response (serializer.data)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        # order_item = order_item.objects.filter(Food__Category = category).count()
        # if order_item>0:
        #     raise ValueError({'details': 'CANNOT DELETE'})
        category.delete()
        return Response({"detail": "Data deleted"})
        
    

# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == "GET":
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response (serializer.data)
           
#     elif request.method =="POST":
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response (serializer.data)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def Category_detail(request, pk):
#     category = Category.objects.get(pk=pk)
#     if request.method == 'GET' :
#         serializer = CategorySerializer(category)
#         return Response (serializer.data)
#     elif request.method == 'PUT':
#         serializer = CategorySerializer(category, data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response (serializer.data)
        
#     elif request.method == 'DELETE':
#         # order_item = order_item.objects.filter(Food__Category = category).count()
#         # if order_item>0:
#         #     raise ValidationError({'details': 'CANNOT DELETE'})
#         category.delete()
#         return Response({"detail": "Data deleted"}, status= status.HTTP_204_No_CONTENT)

# for food category

class FoodViewset(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers

        