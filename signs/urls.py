from django.urls import path
from .views import *

urlpatterns = [
    path('category/', ListCategoryAPIView.as_view(), name='category'),
    path('road-signs/<int:pk>/', ListRoadSignsAPIView.as_view(), name='road-signs'),
]