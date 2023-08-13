from rest_framework import serializers

from restaurants.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name", "publication_date", "restaurant_id", "dishes"]
        read_only_fields = ["publication_date", "restaurant_id"]
