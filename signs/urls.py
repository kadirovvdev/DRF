from django.urls import path
from .views import *

urlpatterns = [
    # path('category/', ListCategoryAPIView.as_view(), name='category'),
    # path('road-signs/<int:pk>/', ListRoadSignsAPIView.as_view(), name='road-signs'),
    # path('create/', CreateListSignsView.as_view(), name='create-list-signs'),
    # path('update/<int:pk>/', RetrieveUpdateDestroyView.as_view(), name='update-list-signs'),
    # path('delete/<int:pk>/', RetrieveUpdateDestroyView.as_view(), name='delete-list-signs'),
    # path('get/<int:pk>/', RetrieveUpdateDestroyView.as_view(), name='get-list-signs'),
    # path('patch/<int:pk>/', RetrieveUpdateDestroyView.as_view(), name='patch-list-signs'),
   
    # path('delete/<int:pk>/', delete, name='delete'),
    # path('get/<int:pk>/', get, name='get'),
    # path('patch/<int:pk>/', patch, name='patch'),
    # path('create/', create, name='create'),
    # path('put/', put, name='put'),

    path('category/', ListCategoryAPIView.as_view(), name='category'),
    path('road-signs/<int:pk>/', ListRoadSignsAPIView.as_view(), name='road-signs'),
    path('create/', CreateAPIView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteAPIView.as_view(), name='delete'),
    path('get/<int:pk>/', GetAPIView.as_view(), name='get'),
    path('patch/<int:pk>/', PatchUpdateAPIView.as_view(), name='patch'),

]