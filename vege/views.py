from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login_page/')
def receipes (request):
  if request.method == "POST":
      data = request.POST
      receipe_image = request.FILES.get('receipe_image')
      receipe_name = data.get('receipe_name')
      receipe_description = data.get('receipe_description')
      print(receipe_name)
      print(receipe_description)
      print(receipe_image)

      Receipe.objects.create(
         receipe_image = receipe_image,
         receipe_name = receipe_name,
         receipe_description = receipe_description 
      )
      return redirect('/')

  if request.GET.get('search'):
     queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
     return redirect('/')
  return render(request,'receipes.html')

def dish(request):
  queryset = Receipe.objects.all()
  context = {'receipes': queryset} 
  return render (request,'dish.html',context)


def delete_receipe (request,id):
   queryset = Receipe.objects.get(id = id)
   queryset.delete()
   return redirect('/')

def update_receipe(request,id):
   queryset = Receipe.objects.get(id = id)
   if request.method == "POST":
      data = request.POST

      receipe_image = request.FILES.get('receipe_image')
      receipe_name = data.get('receipe_name')
      receipe_description = data.get('receipe_description')

      queryset.receipe_name = receipe_name
      queryset.receipe_description = receipe_description

      if receipe_image :
         queryset.receipe_image = receipe_image
      
      queryset.save()
      return redirect('/')



   context = {'receipes': queryset}
   return render (request,'update_receipe.html',context)

def login_page(request):
   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')

      if not User.objects.filter(username = username).exists():
         messages.error(request,'Invalide Username')
         return redirect ('/login_page/')
      
      user = authenticate(username = username,password = password)
      if user is None:
         messages.error(request,'Invalide token . . .')
         return redirect (request, '/login_page/')
      
      else :
         login(request,user)
         return redirect("/")

   return render(request,'login.html')

def register_page(request):
   if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already taken")
            return redirect('/register_page/')

        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name 
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('/register_page/')
   return render(request, 'register.html')

def logout_page(request):
   logout(request)
   return redirect('/login_page/')
