from os import stat
from django.http import JsonResponse
from .models import Recast
from .serializers import RecastSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def recasts(request, format=None):
    if request.method == 'GET':
        recasts = Recast.objects.all()
        serializer = RecastSerializer(recasts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def recast(request, id, format=None):
    try:    
        recast = Recast.objects.get(pk=id)
    except Recast.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecastSerializer(recast)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RecastSerializer(recast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recast.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)