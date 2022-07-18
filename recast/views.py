from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Recast, RecastInst, Actor, Movie, CastInst
from .serializers import UserSerializer, RecastSerializer, RecastInstSerializer, ActorSerializer, MovieSerializer, CastInstSerializer


@api_view(['GET', 'POST'])
def users(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def user(request, id, format=None):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

@api_view(['GET', 'POST'])
def recastInsts(request, format=None):
    if request.method == 'GET':
        recastInsts = RecastInst.objects.all()
        serializer = RecastInstSerializer(recastInsts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecastInstSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def recastInst(request, id, format=None):
    try:    
        recastInst = RecastInst.objects.get(pk=id)
    except RecastInst.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecastInstSerializer(recastInst)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RecastInstSerializer(recastInst, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recastInst.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def actors(request, format=None):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def actor(request, id, format=None):
    try:    
        actor = Actor.objects.get(pk=id)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def movies(request, format=None):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def movie(request, id, format=None):
    try:    
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def castInsts(request, format=None):
    if request.method == 'GET':
        castInsts = CastInst.objects.all()
        serializer = CastInstSerializer(castInsts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CastInstSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def castInst(request, id, format=None):
    try:
        castInst = CastInst.objects.get(pk=id)
    except CastInst.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CastInstSerializer(castInst)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CastInstSerializer(castInst, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        castInst.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)