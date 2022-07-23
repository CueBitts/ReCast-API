"""recast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recast import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'recasts', views.RecastViewSet, basename='recast')
router.register(r'recastinsts', views.RecastInstViewSet, basename='recastinst')
urlpatterns = [path('admin/', admin.site.urls), path('sign-in/', views.userSignIn), path('', include(router.urls))]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', views.users),
#     path('user/<int:id>/', views.user),
#     # should return recasts
#     # path('recasts/', views.RecastViewSet.as_view({'get': 'list'})),
#     # should return recastinsts
#     path('recast/<int:id>/', views.recast),
#     # should return recastinsts
#     path('recastinsts/', views.recastInsts),
#     # unnecessary
#     path('recastinst/<int:id>/', views.recastInst),
#     # unnecessary
#     # path('actors/', views.actors),
#     # path('actor/<int:id>/', views.actor),
#     # # should return recasts
#     # path('movies/', views.movies),
#     # # should return castInsts
#     # path('movie/<int:id>/', views.movie),
#     # # should return castInsts
#     # # should return recasts
#     # path('castinsts/', views.castInsts),
#     # # unnecessary
#     # path('castinst/<int:id>/', views.castInst)
#     # # unnecessary
#     path('', include(router.urls)),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)