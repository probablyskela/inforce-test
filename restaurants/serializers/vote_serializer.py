from rest_framework import serializers

from restaurants.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", "employee_id", "menu_id", "publication_date"]
        read_only_fields = ["employee_id", "menu_id", "publication_date"]
