from rest_framework import serializers
from .models import Przedmioty

class PrzedmiotySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=30)

    def create(self, validated_data):
        return Przedmioty.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def validated_data(self, value):
        if '' in value:
            raise serializers.ValidationError("Nie uzywaj spacji w nazwie przedmiotu")
        return value

