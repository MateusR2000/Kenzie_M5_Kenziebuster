from rest_framework import serializers
from .models import MovieOrder
from movies.serializers import MovieSerializer

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    purchased_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    title = serializers.SerializerMethodField(read_only=True)
    purchased_by = serializers.SerializerMethodField(read_only=True)

    def get_title(self, obj: MovieOrder):
        return obj.movie.title
    
    def get_purchased_by(self, obj: MovieOrder):
        return obj.user.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
    
