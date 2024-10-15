from rest_framework import serializers
from .models import Place, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'comment', 'rating', 'created_at']

class PlaceSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'description', 'category', 'latitude', 'longitude', 'created_at', 'reviews']
