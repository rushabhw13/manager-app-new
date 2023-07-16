"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "CloudTable Manager"
admin.site.site_title = "CloudTable Manager Portal"
admin.site.index_title = "Welcome to CloudTable"

def admin_view_site(request):
    return redirect('/index.html')  # Replace '/index.html' with your desired URL

admin.site.site_url = '/admin-view-site/'  # Replace '/admin-view-site/' with your desired URL pattern

urlpatterns = [
    path("admin/", admin.site.urls),
    path('admin-view-site/', admin_view_site, name='admin_view_site'),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
