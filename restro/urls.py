from django.urls import path
from .views import *

urlpatterns = [
    path('category/', categoryAPIView.as_view()),
    path('category/<pk>', Category_detailAPIVIEW.as_view())
]
