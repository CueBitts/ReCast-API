from urllib.parse import MAX_CACHE_SIZE
from django.db import models


class User(models.Model):
    # id
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    # recast
    # upvotes
    # downvotes

    def __str__(self):
        return self.name

class Recast(models.Model):
    # id
    name = models.CharField(max_length=256)
    # movie = models.ForeignKey('Movie', related_name='recasts', on_delete=models.SET_NULL, null=True)
    movie = models.CharField(max_length=256)
    user = models.ForeignKey(User, related_name='recasts', on_delete=models.CASCADE, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    # recastInst
    upvotes = models.ManyToManyField(User, related_name='upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvotes', blank=True)

    def __str__(self):
        return self.name

class RecastInst(models.Model):
    # id
    recast = models.ForeignKey(Recast, related_name='recastInsts', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    # actor = models.ForeignKey('Actor', related_name='recastInsts', on_delete=models.SET_NULL, null=True)
    actor = models.CharField(max_length=256)
    desc = models.TextField(null=True, blank=True)
    upvotes = models.ManyToManyField(User, related_name='rcupvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='rcdownvotes', blank=True)

    def __str__(self):
        return self.name

# class Actor(models.Model):
#     # id
#     tmdbid = models.CharField(max_length=256)
#     name = models.CharField(max_length=256)
#     img = models.URLField(max_length=1024)
#     # recastInst
#     # castInst

#     def __str__(self):
#         return self.name

# class Movie(models.Model):
#     # id
#     tmdbid = models.CharField(max_length=256)
#     name = models.CharField(max_length=256)
#     img = models.URLField(max_length=1024)
#     # castInst
#     # recast

#     def __str__(self):
#         return self.name

# class CastInst(models.Model):
#     # id
#     movie = models.ForeignKey(Movie, related_name='castInsts', on_delete=models.RESTRICT)
#     name = models.CharField(max_length=256)
#     actor = models.ForeignKey(Actor, related_name='castInsts', on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.name