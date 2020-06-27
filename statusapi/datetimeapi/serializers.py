from rest_framework import serializers
from .models import Parameter


class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter
        fields = ('id','url', 'date')

