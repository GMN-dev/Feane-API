from rest_framework import serializers
from .models import menu, tag

class menuSerializer(serializers.ModelSerializer):   
    class Meta:
        model = menu
        fields = '__all__'


class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = "__all__"

      
class tagSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = ['tag'] 