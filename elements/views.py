from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ImageData
from .serializers import ImageDataSerializer



class ImageDataList(APIView):
    """"List all images we have"""

    def get(self, request):
        images_objects = ImageData.objects.all()
        serializer = ImageDataSerializer(images_objects, many=True)
        return Response(serializer.data)


class ImageDataDetailView(APIView):
    def get(self, request, pk):
        image_object = get_object_or_404(ImageData, pk=pk)
        serializer = ImageDataSerializer(image_object)
        return Response(serializer.data)


