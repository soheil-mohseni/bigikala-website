"""set URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from.import views
app_name= "digi"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('user',views.user,name="user"),
    path('logout',views.logout,name="logout"),
    path('hr',views.hr,name="hr"),
    path('shoe1',views.shoe1,name="shoe1"),
    path('shoe2',views.shoe2,name="shoe2"),
    path('shoe3',views.shoe3,name="shoe3"),
    path('shoe4',views.shoe4,name="shoe4"),
    path('shoe5',views.shoe5,name="shoe5"),
    path('shoe6',views.shoe6,name="shoe6"),
    path('shoe7',views.shoe7,name="shoe7"),
    path('shoe8',views.shoe8,name="shoe8"),
    path('shoe9',views.shoe9,name="shoe9"),
    path('shoe10',views.shoe10,name="shoe10"),
    path('shoe11',views.shoe1,name="shoe11"),
    path('shoe12',views.shoe12,name="shoe12"),

]
