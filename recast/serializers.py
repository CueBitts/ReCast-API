from rest_framework import serializers
from .models import User, Recast, RecastInst, Actor, Movie, CastInst


class RecastInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecastInst
        fields = ['id', 'recast', 'name', 'actor', 'upvotes', 'downvotes']

class RecastSerializer(serializers.ModelSerializer):
    recastInsts = RecastInstSerializer(many=True, read_only=True)
    
    class Meta:
        model = Recast
        fields = ['id', 'name', 'movie', 'user', 'desc', 'recastInsts', 'upvotes', 'downvotes']

class UserSerializer(serializers.ModelSerializer):
    recasts = RecastSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'recasts']

class CastInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastInst
        fields = ['id', 'movie', 'name', 'actor']

class ActorSerializer(serializers.ModelSerializer):
    recastInsts = RecastInstSerializer(many=True, read_only=True)
    castInsts = CastInstSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = ['id', 'tmdbid', 'name', 'img', 'recastInsts', 'castInsts']

class MovieSerializer(serializers.ModelSerializer):
    castInsts = CastInstSerializer(many=True, read_only=True)
    recasts = RecastSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'tmdbid', 'name', 'img', 'castInsts', 'recasts']