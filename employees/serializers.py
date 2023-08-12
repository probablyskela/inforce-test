from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "email", "first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data: dict):
        password = validated_data.pop("password", None)
        user = Employee(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
