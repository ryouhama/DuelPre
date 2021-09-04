from django.db.models import fields
from rest_framework import serializers
from card.models.card import models

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = '__all__'

class CivilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Civilization
        fields = '__all__'

class CardFetchSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Card
        fields = '__all__'

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['civilizations'] = CivilizationSerializer(data=instance.civilizations, many=True)
