from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Parameter
from .serializers import ParameterSerializer
from django.http import JsonResponse

class DateTimeParameter(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
# @csrf_exempt
# def parameter_list(request):
#     """
#     List all code parameter, or create a new parameter.
#     """
#     if request.method == 'GET':
#         parameter = Parameter.objects.all()
#         serializer = ParameterSerializer(parameter, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ParameterSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def parameter_detail(request, pk):
#     """
#     Retrieve, update or delete a code parameter.
#     """
#     try:
#         parameter = Parameter.objects.get(pk=pk)
#     except Parameter.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ParameterSerializer(parameter)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ParameterSerializer(parameter, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         parameter.delete()
#         return HttpResponse(status=204)


def health_check(request):
    data = {"status": "ok"}
    return JsonResponse(data)
