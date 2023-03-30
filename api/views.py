from rest_framework.response import Response
from rest_framework.views import APIView 
from .serializer import tagSerializer, menuSerializer, tagSerializerPost
from .models import menu, tag
from rest_framework import status


class menuAPI(APIView):
    def get(self, request):
        if request.method == "GET":
            # Seleciona todos as instancias no banco de dados
            menuList = menu.objects.filter(status=True)
            # Serializa os dadoss
            serializer = menuSerializer(menuList, many=True, context={'request': request})
            #verificação se os dados correpondem ao serializer definido
            if serializer.is_valid:
                # Resposta com todos os dados
                return Response(serializer.data, status=status.HTTP_200_OK)

                #Resposta caso erro
            else:
                return Response({"Message":"Error"})


class tagApi(APIView):
    def get(self, request):
        if request.method == "GET":
            # Seleciona todos as instancias no banco de dados
            tagList = tag.objects.filter(status=True)
            # Serializa os dadoss
            serializer = tagSerializerPost(tagList, many=True, context={'request': request})
            #verificação se os dados correpondem ao serializer definido
            if serializer.is_valid:
                # Resposta com todos os dados
                return Response(serializer.data, status=status.HTTP_200_OK)
                #Resposta caso erro
            else:
                return Response({"Message":"Error"})
    
    def post(self, request):
        if request.method == 'POST':
            serializer = tagSerializerPost(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"Message":"Error"}, status=status.HTTP_404_NOT_FOUND)


    



