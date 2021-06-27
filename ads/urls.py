"""propsell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Loginuser,APropertyHome,APropdel,LoginAdminuser,APropertyViewEdit,registeruser,UserProf,PropertyViewCity,userdel,PropertyView,PropertyViewEdit,PropertyHome,userview,useredit

urlpatterns = [
    path('login',Loginuser.as_view()),
    path('register',registeruser.as_view()),
    path('prof/<int:id>',UserProf.as_view()),
    path('post/<str:uname>',PropertyView.as_view()),
    path('postedi/<int:id>/',PropertyViewEdit.as_view()),
    path('apostedi/<int:id>/',APropertyViewEdit.as_view()),
    path('home',PropertyHome.as_view()),
    path('ahome',APropertyHome.as_view()),
    path('propdel/<int:id>',APropdel.as_view()),
    path('users',userview.as_view()),
    path('useredit',useredit.as_view()),
    path('loginadmin',LoginAdminuser.as_view()),
    path('userdel/<str:uname>',userdel.as_view()),
    path('postcity/<str:city>',PropertyViewCity.as_view())

]
