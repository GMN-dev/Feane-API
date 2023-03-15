from rest_framework.response import Response
from rest_framework.views import APIView 
from .serializer import tagSerializer, menuSerializer
from .models import menu
from rest_framework import status
from rest_framework.decorators import api_view

# from django.shortcuts import get_object_or_404

class menuAPI(APIView):
    def get(self, request):
        if request.method == "GET":
            menuList = menu.objects.all()
            serializer = menuSerializer(menuList, many=True)
            if serializer.is_valid:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"Message":"Error"})
    
    



