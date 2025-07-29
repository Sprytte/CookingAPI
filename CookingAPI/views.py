from rest_framework.utils import json

from CookingAPI.models import *
from CookingAPI.serializer import *
from django.http import JsonResponse, HttpResponse, HttpRequest
from datetime import datetime, timedelta, time
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view

def recipes(request):
    # params = request.META["QUERY_STRING "].split(",")
    data = Recipe.objects.all()
    serializer = RecipeSerializer(data, many=True)
    return JsonResponse({'recipes': serializer.data})

def test(request):
    if request.method == "POST":
        data = request.POST
        dur = data.get("duration")
        dic_raw = data.get("list")
        dic = []
        count = 1
        for d in dic_raw.split(','):
            # dic[count] = d
            dic.append(d)
            count += 1
        temp = Test(time_test= time(minute=int(data.get("time"))),
                    duration=timedelta(hours=int(dur.split(',')[0]), minutes=int(dur.split(',')[1])),
                    list=dic,
                    int_list=data.get("ints"))
        Test.save(temp)
        print(temp.list)
        print(temp.list[1])
        data = Test.objects.filter(pk=temp.pk)
    else:
        data = Test.objects.all()
    serializer = TestSerializer(data, many=True)
    return JsonResponse({'test': serializer.data})

# @api_view(["POST"])
def nationalities(request):
    if request.method == "POST":
        data = request.POST
        new_nationality = Nationality(name=(data.get("name")))
        Nationality.save(new_nationality)
        data = Nationality.objects.filter(pk=new_nationality.pk)
    else:
        data = Nationality.objects.all()
    serializer = NationalitySerializer(data, many=True)
    return JsonResponse({'nationalities': serializer.data})
def single_nationality(request, nation_id):
    nationality = Nationality.objects.get(pk=nation_id)
    serializer = NationalitySerializer(instance=nationality)
    if request.method == "DELETE":
        nationality.delete()

    return JsonResponse({'nationality': serializer.data})

def categories(request):
    if request.method == "POST":
        data = request.POST
        new_type = RecipeType(name=(data.get("name")))
        RecipeType.save(new_type)
        data = RecipeType.objects.filter(pk=new_type.pk)
    else:
        data = RecipeType.objects.all()
    serializer = TypeSerializer(data, many=True)
    return JsonResponse({'categories': serializer.data})
def single_category(request, type_id):
    category = RecipeType.objects.get(pk=type_id)
    serializer = TypeSerializer(instance=category)
    if request.method == "DELETE":
        category.delete()

    return JsonResponse({'category': serializer.data})

def tempQueries():
    r1 = Recipe.objects.all() #get all recipes
    r2 = Recipe.objects.get(pk=1) #get recipe by (auto) id
    r3 = Recipe.objects.filter(recipe_name__contains='Lasagna') #get recipes with lasagna in name
    r4 = Recipe.objects.exclude(portion__lt=5) #get all recipes that have MORE than 4 portion
    r5 = Recipe.objects.filter(recipesection__section_time__minute__lte=30) #gets recipes where at
    # least one section takes <= 30min
    r6 = Recipe.objects.filter()