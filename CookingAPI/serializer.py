from rest_framework import serializers
from CookingAPI.models import *

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeSection
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeType
        fields = '__all__'
class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'