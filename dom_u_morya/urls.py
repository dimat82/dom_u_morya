"""dom_u_morya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from houses.views import *
from django.conf.urls.static import static
from django.conf import settings
import houses.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', houses_list, name = 'base'),
    path('house_detail/<int:house_id>/', house_detail, name = 'house_detail'),
    path('houses/', include('houses.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

