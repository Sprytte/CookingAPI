from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from CookingAPI.models import *
from CookingAPI.serializer import *
from django.http import JsonResponse, HttpResponse, HttpRequest
from datetime import datetime, timedelta, time
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view

def recipes(request):
    # params = request.META["QUERY_STRING "].split(",")
    if request.method == "POST":
        data = request.POST
        new_recipe = add_recipe(data)
        new_recipe.save()
        data = Recipe.objects.filter(pk=new_recipe.pk)
    else:
        data = Recipe.objects.all()
    serializer = RecipeSerializer(data, many=True)
    return JsonResponse({'recipes': serializer.data})
@api_view(['GET', 'PUT', 'DELETE'])
def single_recipe(request: Request, id):
    recipe = Recipe.objects.get(pk=id)
    serializer = RecipeSerializer(instance=recipe)
    if request.method == "PUT":
        print(request.data)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.data['cook_time'] = time.min
            serializer.save()
    elif request.method == "DELETE":
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return JsonResponse({'recipe': serializer.data})

# def sections(request, recipe_id):
#     if request.method == "POST":
#         data = request.POST
#         new_section = RecipeSection(name=(data.get("name"))) #modify recipe cook time
#         RecipeSection.save(new_section)
#         data = RecipeSection.objects.filter(pk=new_section.pk)
#     else:
#         data = RecipeSection.objects.all()
#     serializer = SectionSerializer(data, many=True)
#     return JsonResponse({'sections': serializer.data})

# @api_view(["POST"])
def nationalities(request):
    if request.method == "POST":
        data = request.POST
        new_nationality = Nationality(name=(data.get("name")))
        new_nationality.save()
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
        new_type.save()
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

def add_recipe(data):
    temp_ingred = []
    temp_img = []
    if isinstance(data.get("ingredients"), str):
        for i in data.get("ingredients").split(";"):
            temp_ingred.append(i)
    elif isinstance(data.get("images"), str):
        for i in data.get("images").split(";"):
            temp_img.append(i)
    else:
        temp_ingred = data.get("ingredients")
        temp_img = data.get('images')
    new_recipe = Recipe(recipe_name=data.get("name"),
                        ingredients=temp_ingred,
                        type=data.get('type'),
                        nationality=Nationality.objects.get(pk=int(data.get('nationality'))),
                        source=data.get('source'),
                        portion=int(data.get('portion')),
                        creator=data.get('creator'),
                        # cook_time=time(hour=int(data.get('hour')), minute=int(data.get('minute'))),
                        cook_time=time.min,
                        image_links=temp_img)

    return new_recipe

def tempQueries():
    r1 = Recipe.objects.all() #get all recipes
    r2 = Recipe.objects.get(pk=1) #get recipe by (auto) id
    r3 = Recipe.objects.filter(recipe_name__contains='Lasagna') #get recipes with lasagna in name
    r4 = Recipe.objects.exclude(portion__lt=5) #get all recipes that have MORE than 4 portion
    r5 = Recipe.objects.filter(recipesection__section_time__minute__lte=30) #gets recipes where at
    # least one section takes <= 30min
    r6 = Recipe.objects.filter()