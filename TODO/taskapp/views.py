from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginuser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from taskapp.forms import TODOforms
from taskapp.models import TODO
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
   form = TODOforms()
   if request.user.is_authenticated:
        user = request.user
        todos = TODO.objects.filter(user = user).order_by('priority')
        context = {
        'form' : form,
        'todos' : todos,
        }
        return render (request , 'main.html' , context=context)

def login(request):
   if request.method == 'GET':
         form = AuthenticationForm()
         context = {
         "form" : form,
         }
         return render(request, "login.html", context=context)
   
   else:
       form = AuthenticationForm(data = request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username , password=password)
           print("Authenticate" ,user)
           if user is not None:
               loginuser(request,user)
               return redirect('index')
       else:
           context = {
           "form" : form,
           }
           return render(request, "login.html", context=context)
   
           
 
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
        "form" : form,
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
        "form" : form,
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')

        else:
             return render(request,'signup.html' , context=context)
        

def add_task(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOforms(request.POST)
        context = {
        'form' : form
          }
        if form.is_valid():
          print(form.cleaned_data)
          todo = form.save(commit=False)
          todo.user = user
          todo.save()
          print(todo)
          return redirect ('index')
        else:
          return render (request , 'main.html' , context=context)


def signout(request):
    logout(request)
    return redirect ('login')

def delete_task(request ,id):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect ('index')