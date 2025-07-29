"""
URL configuration for CookingAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from CookingAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', include('django.contrib.auth.urls')),
    path('api/recipes/', views.recipes, name='recipes'),
    path('api/recipes/<int:id>/', views.single_recipe, name='recipe'),
    path('api/nationalities/', views.nationalities, name='nationalities'),
    path('api/nationalities/<int:nation_id>/', views.single_nationality, name='nationality'),
    path('api/categories/', views.categories, name='categories'),
    path('api/categories/<int:type_id>/', views.single_category, name='category'),
    # path('api/sections/', views.sections, name='sections'),
]
