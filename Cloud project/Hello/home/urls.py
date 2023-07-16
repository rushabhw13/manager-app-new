from django.contrib import admin
from django.urls import path
from home import views
from .views import update_todays_special



urlpatterns = [
    path('', views.api_list, name='api_list'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('staff/', views.staff, name='staff'),
    path('todayspecial/', views.todays_special, name='todays_special'),
    path('todayspecial/update/<int:pk>/', views.update_todays_special, name='update_todays_special'),
    path('tables/', views.tables, name='tables'),
]

