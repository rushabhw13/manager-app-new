from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import TodayspecialForm
from django.contrib.auth import authenticate, login, logout
import json
from .models import Restaurant, Staff, Menu, Tables, Todayspecial
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page after successful login
        else:
            # Handle invalid credentials error
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login') 


def index(request):
    restaurant = Restaurant.objects.first() 
    context = {'restaurant': restaurant}
    return render(request, 'index.html', context)


def menu(request):
    menus = Menu.objects.all() 
    context = {'menus': menus}
    return render(request, 'menu.html', context)

@api_view(['GET'])
def staff(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff.html', {'staff_members': staff_members})



def todays_special(request):
    specials = Todayspecial.objects.all()
    context = {'specials' : specials}
    return render(request, 'todayspecial.html', context)

def update_todays_special(request, pk):
    special = Todayspecial.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodayspecialForm(request.POST, instance=special)
        if form.is_valid():
            form.save()
            return redirect('todays_special')
    else:
        form = TodayspecialForm(instance=special)
    context = {'form': form}
    return render(request, 'update_todayspecial.html', context)

def tables(request):
    if request.method == 'GET':
        tables = Tables.objects.all()
        context = {'tables': tables}
        return render(request, 'tables.html', context)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_list(request):
    """
    List all the available APIs.
    """
    api_urls = {
        'Login API': 'http://127.0.0.1:8000/login/',
        'Index API': 'http://127.0.0.1:8000/index/',
        'Menu API': 'http://127.0.0.1:8000/menu/',
        'Staff API': 'http://127.0.0.1:8000/staff/',
        'Today\'s Special API': 'http://127.0.0.1:8000/todayspecial/',
        'Tables API': 'http://127.0.0.1:8000/tables/',
        'Logout API': 'http://127.0.0.1:8000/logout/',
    }

    return Response(api_urls)