"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from config.views import logout_view
from page.views import home_view

urlpatterns = [
    path('', home_view, name='home'),

    # Todo Apps:
    path('todo/', include('todo.urls', namespace='todo')),

    # Auth:
    path('account/logout/', logout_view, name='logout_view'),
    # Admin:
    path("admin/", admin.site.urls),
]
