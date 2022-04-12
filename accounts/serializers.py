from rest_framework import serializers
from .models import Register


class RegisterSerializer(serializers.ModelSerializer):



    class Meta:
        fields = ('name', 'email', 'password', 'password2', )
        model = Register