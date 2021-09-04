from typing import Any, Dict
from library.card.models.card import models
from library.card.serializers.card import serializer
from django.db.models import BaseManager

class CardAdapter():
    model_data: BaseManager[models.Card]

    def serialize(self) -> Dict[str, Any]:
        related_model_data = serializer.CardSerializer.eager_load(self.model_data)
        return serializer.CardSerializer(related_model_data, partial=True).data
