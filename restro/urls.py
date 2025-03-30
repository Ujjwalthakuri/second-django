from django.urls import path
from .views import *

urlpatterns = [
    path('category/', category_list),
    path('category/<pk>', Category_detail)
]
