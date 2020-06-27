from django.urls import path, include
from .import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register('api', views.DateTimeParameter)

urlpatterns = [
    # path('parameter/',views.parameter_list),
    # path('parameter/<int:pk>/',views.parameter_detail),
    path('',include(router.urls)),
    path('',views.health_check, name='health_check'),
]


