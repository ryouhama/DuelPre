from django.db.models.manager import BaseManager
from rest_framework import serializers
from card.models.card import models


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = '__all__'

    @classmethod
    def eager_load(cls, model_data: BaseManager[models.Card]) -> BaseManager[models.Card]:
        return model_data.prefetch_related(
            'civilization__civilizations'
        )


class CivilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Civilization
        fields = '__all__'


class CardFetchSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Card
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['civilizations'] = CivilizationSerializer(data=instance.civilizations, many=True)
