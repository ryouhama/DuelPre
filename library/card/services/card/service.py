from typing import Any, Dict
from rest_framework.utils.serializer_helpers import ReturnDict
from card.models.card.models import Card
from card.serializers.card.serializer import CardSerializer, CardFetchSerializer, CivilizationSerializer

class CardService:

    def exists(self, card_id: int) -> bool:
        return Card.objects.filter(id=card_id).exists()

    def get(self, card_id: int) -> ReturnDict:
        card = Card.objects.get(id=card_id)
        serializer = CardSerializer(card, partial=True)
        return serializer.data

    def fetch(self) -> ReturnDict:
        cards = Card.objects.prefetch_related('civilizations').all()
        serializer = CardFetchSerializer(cards, many=True)
        return serializer.data

    def create(self, data: Dict[str, Any]) -> ReturnDict:
        civilizations = data.pop('civilizations', None)

        card_serializer = CardSerializer(data=data, partial=True)
        if card_serializer.is_valid():
            created_card = card_serializer.save()
        else:
            raise Exception(card_serializer.errors)

        civilization_serializer = CivilizationSerializer(data=civilizations, many=True)
        if civilization_serializer.is_valid():
            created_civilization = civilization_serializer.save()
        else:
            raise Exception(civilization_serializer.errors)

        # CardとCivilizationを紐付け
        update_coloms_dict = {
            'civilizations': [it.pk for it in created_civilization]
        }
        update_card_serializer = CardSerializer(created_card, update_coloms_dict, partial=True)
        if update_card_serializer.is_valid():
            update_card_serializer.save()
        else:
            raise Exception(update_card_serializer.errors)

        return CardSerializer(update_card_serializer)