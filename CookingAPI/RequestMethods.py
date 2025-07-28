from django.http import HttpResponse, HttpRequest, HttpHeaders
from CookingAPI.models import Recipe, RecipeSection
import datetime


def get_recipes(request=HttpRequest):
    # now = datetime.datetime.now()
    # html = '<html lang="en"><body>It is now %s.</body></html>' % now
    # return HttpResponse(html)
    params = request.META["QUERY_STRING "].split(",")
    recipes = Recipe.objects.get()
    return HttpResponse(recipes)

# if request.method == "GET":
#     do_something()
# elif request.method == "POST":
#     do_something_else()