from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PhotoSerializer


def index(request):
    return render(request, 'api/index.html')


class PhotoList(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        # serializer = PhotoSerializer(data=request.data, files=request.files)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("OKs", status=status.HTTP_201_CREATED)