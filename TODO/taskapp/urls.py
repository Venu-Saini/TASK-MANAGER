from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('login/', views.login , name = 'login' ),
    path('signup/', views.signup , name = 'signup' ),
    path('add_task/',views.add_task, name = 'add_task'),
    path('delete_task/<int:id>', views.delete_task , name = 'delete_task'),
    path('logout/', views.signout, name='logout'),
    
]
