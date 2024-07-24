"""
Serializer for recipe APISs
"""
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description', 'image']


class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading image to recipe."""

    class Meta:
        model = Recipe
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': True}}