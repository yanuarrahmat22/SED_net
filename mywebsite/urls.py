"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blog_views.index),
    path('home', blog_views.index, name='home'),
    path('reupload_images', blog_views.reupload_images),
    path('del_images', blog_views.del_images),
    path('predict_image', blog_views.predict_image, name = 'predict_image'),
    path('get_images', blog_views.get_images, name = 'get_images'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)