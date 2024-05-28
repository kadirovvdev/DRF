from django.contrib.messages import success
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

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


class CreateAPIView(APIView):
    def post(self, request):
        serializer = RoadSignsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class UpdateAPIView(APIView):
    def put(self, request, pk):
        road_signs = RoadSigns.objects.get(pk=pk)
        serializer = RoadSignsSerializer(road_signs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAPIView(APIView):
    def delete(self, pk):
        road_signs = RoadSigns.objects.get(pk=pk)
        road_signs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class GetAPIView(APIView):
    def get(self, request, pk):
        road_signs = RoadSigns.objects.get(pk=pk)
        serializer = RoadSignsSerializer(road_signs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PatchUpdateAPIView(APIView):
    def patch(self, request, pk):
        road_signs = RoadSigns.objects.get(pk=pk)
        serializer = RoadSignsSerializer(road_signs, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
# class CreateListSignsView(ListCreateAPIView):
#     queryset = RoadSigns.objects.all()
#     serializer_class = RoadSignsSerializer
#
#
# class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = RoadSigns.objects.all()
#     serializer_class = RoadSignsSerializer

# @api_view(['POST'])
# def create(request):
#     serializer = RoadSignsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['PUT'])
# def put(request):
#     road_signs = RoadSigns.objects.all()
#     serializer = RoadSignsSerializer(road_signs, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['DELETE'])
# def delete(pk):
#     road_signs = RoadSigns.objects.get(pk=pk)
#     road_signs.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET'])
# def get(request, pk):
#     road_signs = RoadSigns.objects.get(pk=pk)
#     serializer = RoadSignsSerializer(road_signs, many=False)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['PATCH'])
# def patch(request, pk):
#     road_signs = RoadSigns.objects.get(pk=pk)
#     serializer = RoadSignsSerializer(road_signs, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




