from django.contrib import admin
from .models import User, Recast, RecastInst
# , Actor, Movie, CastInst


admin.site.register(User)
admin.site.register(Recast)
admin.site.register(RecastInst)
# admin.site.register(Actor)
# admin.site.register(Movie)
# admin.site.register(CastInst)