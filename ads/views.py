from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout, authenticate
from .models import Userinfo,Property
from .decorators import adminonly,adminonly3,adminonly2

from.serializers import RegisterUserSerializer,LoginSerializer,PropSerializer
# Create your views here.
class registeruser(APIView):
    def post(self,request):
        serializer=RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Loginuser(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            # user=authenticate(request,username=username,password=password)
            user=Userinfo.objects.get(username=username)
            if (user.username==username)&(user.password==password):
                login(request,user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token":token.key},status=status.HTTP_201_CREATED)
            else:
                return Response("serializer.errors",status=status.HTTP_400_BAD_REQUEST)



class LoginAdminuser(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=username,password=password)
            # user=Userinfo.objects.get(username=username)
            # if (user.username==username)&(user.password==password)&(user.is_superuser==True):
            login(request,user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=status.HTTP_201_CREATED)
        else:
            return Response("Incorrect Username/Password",status=status.HTTP_400_BAD_REQUEST)

class UserProf(APIView):
    def get(self,request,id):
        user=Userinfo.objects.get(id=id)
        serializer=RegisterUserSerializer(user)
        return Response(serializer.data)
    def put(self,request,id):
        user=Userinfo.objects.get(id=id)
        serializer=RegisterUserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        user = Userinfo.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @method_decorator(adminonly3,name='dispatch')
class userdel(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def delete(self,request,uname):
        user=Userinfo.objects.get(username=uname)
        ads=Property.objects.filter(uname=uname)
        user.delete()
        ads.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PropertyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,uname):
        request.data["uname"]=uname
        serializer=PropSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,uname):
        prop=Property.objects.filter(uname=uname)
        serializer=PropSerializer(prop,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class APropertyViewEdit(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        prop = Property.objects.filter(id=id)
        serializer = PropSerializer(prop,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PropertyViewEdit(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        prop = Property.objects.filter(id=id)
        serializer = PropSerializer(prop,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        prop = Property.objects.get(id=id)
        serializer = PropSerializer(prop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        prop=Property.objects.get(id=id)
        prop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PropertyViewCity(APIView):
    def get(self, request, city):
        prop = Property.objects.filter(city=city)
        serializer = PropSerializer(prop,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PropertyHome(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        prop = Property.objects.all()
        serializer = PropSerializer(prop,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# @method_decorator(adminonly,name='dispatch')
class APropdel(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def delete(self, request, id):
        prop=Property.objects.get(id=id)
        prop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# @method_decorator(adminonly2,name='dispatch')
class APropertyHome(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get(self, request):
        prop = Property.objects.all()
        serializer = PropSerializer(prop,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# @method_decorator(adminonly2,name='dispatch')
class userview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get(self,request):
        # if request.user.is_superuser:
        user=Userinfo.objects.filter(is_staff=False)
        serializer=RegisterUserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        # else:
        #     return Response("Login required", status=status.HTTP_401_UNAUTHORIZED)

# @method_decorator(adminonly,name='dispatch')
class useredit(APIView):
    # def put(self,request,id):
    #     user=Userinfo.objects.get(id=id)
    #     serializer=RegisterUserSerializer(user,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, id):
        prop = Userinfo.objects.get(id=id)
        prop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


