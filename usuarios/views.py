from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsuariosSerializers
from .models import Usuario
# Create your views here.
class UsuariosAPIView(APIView):

    def post(self, request):
        serializer = UsuariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        correo = request.GET.get('correo')
        if (correo is None):
            try:
                usuarios = Usuario.objects.all()         
            except Usuario.DoesNotExist:
                return Response()
            
            serializer = UsuariosSerializers(usuarios, many= True)
            return Response(serializer.data)
        else:
            try:
                usuarios = Usuario.objects.get(correo=correo)
            except Usuario.DoesNotExist:
                return Response({'Error': 'El correo no existe'})

            serializer = UsuariosSerializers(usuarios, many=False)
            return Response(serializer.data)