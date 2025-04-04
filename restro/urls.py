from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category',CategoryViewset, basename= 'category' )
router.register(r'food',FoodViewset, basename='food' )

urlpatterns = [
    # path('category/', CategoryViewset.as_view({'get': 'list', 'post': 'create'})),
    # path('category/<pk>', Category_detailAPIVIEW.as_view())
]+router.urls
