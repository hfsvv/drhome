from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Userinfo,Property,Propertys
from rest_framework import serializers

class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model=Userinfo
        fields=["username","first_name","last_name","password","email","mobno","dob","place","prof_pic"]

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class PropSerializer(ModelSerializer):
    class Meta:
        model=Propertys
        fields="__all__"
