from django.core.validators import RegexValidator, int_list_validator
from django.db import models

# TODO sqlite requires json extension
class Nationality(models.Model):
    name = models.CharField('50')
class RecipeType(models.Model):
    name = models.CharField('25')

class Recipe(models.Model):
    #debatably useful/important
    recipe_id = models.UUIDField()

    recipe_name = models.CharField(max_length=50)
    ingredients = models.JSONField()  #tuple nb/text? For converting when adjusting portion
    type = models.CharField(validators=[int_list_validator()]) #not sure if multiple selection.
    # Validation when type deleted?
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_DEFAULT, default=0) #Can create new choice with method Fruit.objects.create(name="Apple").
    # on_delete=models.DO_NOTHING
    source = models.CharField(max_length=50)
    # sections = models.CharField(validators=[int_list_validator()]) #maybe
    portion = models.IntegerField()
    creator = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50) #tuple nb/text? purely minutes? Auto adjust from section times
    date_created = models.DateTimeField()
    image_links = models.JSONField()


class RecipeSection(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=50)
    steps = models.JSONField()
    section_time = models.TimeField() #could make int? only min then formatted later?
    section_order = models.IntegerField()

    # private List < String > steps;

class Test(models.Model):
    duration = models.DurationField()
    list = models.JSONField()
    time_test = models.TimeField()
    int_list = models.CharField(validators=[int_list_validator()])