from django.db.models.manager import BaseManager
from rest_framework import serializers
from card.models.card import models


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        civilizations = [
            it.civilization for it in instance.civilizations.all()
        ]
        civilization_serializer = CivilizationSerializer(
            data=civilizations, many=True)
        civilization_serializer.is_valid()
        data['civilizations'] = civilization_serializer.data
        return data


class CardCivilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardCivilization
        fields = '__all__'


class CivilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Civilization
        fields = '__all__'


class CardFetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        civilizations = [
            it.civilization for it in instance.civilizations.all()
        ]
        civilization_serializer = CivilizationSerializer(
            data=civilizations, many=True)
        civilization_serializer.is_valid()
        data['civilizations'] = civilization_serializer.data
        return data

    @classmethod
    def eager_load(
        cls,
        model_data: BaseManager[models.Card]
    ) -> BaseManager[models.Card]:
        return model_data.prefetch_related(
            'civilizations__civilization'
        )
