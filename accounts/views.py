from rest_framework import generics
from .models import Register
from.serializers import RegisterSerializer



class RegisterList(generics.ListAPIView):
    queryset= Register.objects.all()
    serializer_class = RegisterSerializer




class RegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Register.objects.all()
    serializer_class = RegisterSerializer
   

