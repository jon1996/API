from rest_framework import serializers
from .models import reportModel
from rest_framework.fields import ChoiceField


class reportSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
   
    class Meta:
        model = reportModel
        fields = '__all__'