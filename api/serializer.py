from rest_framework import serializers
from .models import menu, tag

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = "__all__"

      
class tagSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = ['name'] 


class menuSerializer(serializers.ModelSerializer):   
    tag = tagSerializerPost()

    class Meta:
        model = menu
        fields = '__all__'
