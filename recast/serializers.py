from rest_framework import serializers
from .models import User, Recast, RecastInst, Actor, Movie, CastInst


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'recasts']

class CastInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastInst
        fields = ['id', 'movie', 'name', 'actor']

class ActorSerializer(serializers.ModelSerializer):
    castInsts = CastInstSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = ['id', 'tmdbid', 'name', 'img', 'recastInsts', 'castInsts']

class RecastInstSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(read_only=True)
    
    class Meta:
        model = RecastInst
        fields = ['id', 'recast', 'name', 'actor', 'upvotes', 'downvotes']

class MovieSerializer(serializers.ModelSerializer):
    castInsts = CastInstSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'tmdbid', 'name', 'img', 'castInsts', 'recasts']

class RecastSerializer(serializers.ModelSerializer):
    class Meta:
        movie = MovieSerializer(read_only=True)
        user = UserSerializer(read_only=True)
        recastInsts = RecastInstSerializer(many=True, read_only=True)
        
        model = Recast
        fields = ['id', 'name', 'movie', 'user', 'desc', 'recastInsts', 'upvotes', 'downvotes']
        depth = 2







