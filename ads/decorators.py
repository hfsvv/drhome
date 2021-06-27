from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status

def adminonly(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return Response("Login Required",status=status.HTTP_400_BAD_REQUEST)
        else:
            return func(request,id)
    return wrapper

def adminonly2(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return Response("Login Required",status=status.HTTP_400_BAD_REQUEST)
        else:
            return func(request)
    return wrapper
def adminonly3(func):
    def wrapper(request,uname):
        if not request.user.is_superuser:
            return Response("Login Required",status=status.HTTP_400_BAD_REQUEST)
        else:
            return func(request,uname)
    return wrapper