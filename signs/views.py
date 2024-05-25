from django.contrib.messages import success
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from.models import *

# Create your views here.

class ListCategoryAPIView(APIView):
    def get(self, request):
        category = CategorySigns.objects.all()
        serializers = CategorySignsSerializer(category, many=True)
        return Response(
            {
                'category': serializers.data,
                'status': 'success',
                'status_code': status.HTTP_200_OK

            })

class ListRoadSignsAPIView(APIView):
    def get(self, request, pk):
        road_signs = RoadSigns.objects.filter(pk=pk)
        serializers = RoadSignsSerializer(road_signs, many=True)
        return Response(
            {
                'road_signs': serializers.data,
                'status': 'success',
                'status_code': status.HTTP_200_OK

            })


