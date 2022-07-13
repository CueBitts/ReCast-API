from django.http import JsonResponse
from .models import Recast
from .serializers import RecastSerializer

def recasts(request):
    recasts = Recast.objects.all()
    serializer = RecastSerializer(recasts, many=True)
    return JsonResponse({'data': serializer.data})