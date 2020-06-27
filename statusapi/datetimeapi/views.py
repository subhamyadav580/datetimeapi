from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Parameter
from .serializers import ParameterSerializer
from django.http import JsonResponse


"""
   List all code snippets, or create a new snippet.
   Retrieve, update or delete a code snippet.
"""
class DateTimeParameter(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer



def status_check(request):
    data = {"status": "ok"}
    return JsonResponse(data)
