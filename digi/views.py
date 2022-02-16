from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from .models import product , basket
# Create your views here.


def signup(request):
    if request.method == 'POST':
        
        if request.POST['password1'] == request.POST['password2']: 
            try: 

                user = User.objects.get(username=request.POST['username']) 


                return render(request, 'account/signup.html', {'error':'Username has already been taken!'})
            except User.DoesNotExist: 

                user = User.objects.create_user(request.POST['username'], request.POST['email'] ,    request.POST['password1'])
                auth.login(request,user)
                return render(request, 'bigikala/index.html')
                
                
 
        else: # در صورتی که دوتا پسورد باهم همخوانی نداشته باشه
            alerts = 'samba' 
            contex = {
           'alert' : alerts,  
    
            }
            return render(request,'bigikala/signup.html', contex)
    else:

        return render(request, 'bigikala/signup.html')
        
        
def home(request):
    return render(request, 'bigikala/index.html')
    
def user(request):
    return redirect('http://127.0.0.1:8000/accounts/login/')


def logout(request):
    return redirect('http://127.0.0.1:8000/accounts/logout/')    
    
  
    
    
    
    
    
def hr (request):
    baskets = basket.objects.all()
    contex = {"basket": baskets}
    return render(request,"bigikala/basket.html",contex)




def shoe1 (request):
    baskets = basket()
    myprice= product.objects.get(price=90)
    baskets.money=myprice.price
    baskets.metal = product.objects.get(name="کفش های قرمز metcon")
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')
    
def shoe2 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش های آبی metcon")
    myprice= product.objects.get(price=100)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')



    

def shoe3 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش های زرد metcon")
    myprice= product.objects.get(price=80)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')
    

def shoe4 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش های نایک مدل اول")
    myprice= product.objects.get(price=141)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')


def shoe5 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش های نایک مدل دوم")
    myprice= product.objects.get(price=151)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')


def shoe6 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش های نایک مدل سوم")
    myprice= product.objects.get(price=111)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')
    
    
def shoe7 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش های نایک مدل چهارم")
    myprice= product.objects.get(price=121)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')  
    


def shoe8 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش های نایک مدل پنجم")
    myprice= product.objects.get(price=131)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')



def shoe9 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش های نایک مدل شیشم")
    myprice= product.objects.get(price=121)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')
    
    
    
def shoe10 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش جدید نایک ایرمکس تمام مشکی")
    myprice= product.objects.get(price=81)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')
    
    
    
def shoe11 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش جدید نایک ایرمکس تمام سفید")
    myprice= product.objects.get(price=71)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')
    
    
    
def shoe12 (request):
    baskets = basket()
    baskets.metal = product.objects.get(name="کفش  نایک ایرمکس مشکی و سفید")
    myprice= product.objects.get(price=101)
    baskets.money=myprice.price
    baskets.user = request.user
    baskets.save()
    return render(request, 'bigikala/index.html')
