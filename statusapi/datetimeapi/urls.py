from django.urls import path, include
from .import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register('api', views.DateTimeParameter)

urlpatterns = [
    path('',include(router.urls)),
    path('',views.health_check, name='status_check'),
]


