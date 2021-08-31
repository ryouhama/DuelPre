from rest_framework.utils.serializer_helpers import ReturnDict
from card.models.card.models import Card
from card.seliarizers.card.serializer import CardSerializer

class CardService:

    def exists(self, card_id: int) -> bool:
        return Card.objects.filter(id=card_id).exists()


    def get(self, card_id: int) -> ReturnDict:
        card = Card.objects.get(id=card_id)
        serializer = CardSerializer(card, partial=True)
        return serializer.data