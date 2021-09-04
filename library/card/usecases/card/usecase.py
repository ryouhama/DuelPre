from typing import Any, Dict
from card.services.card.service import CardService


class CardUsecase:

    def get(self, card_id: int):
        service = CardService()
        return service.get(card_id) if service.exists(card_id) else {}

    def fetch(self):
        service = CardService()
        return service.fetch()

    def create(self, data: Dict[str, Any]):
        service = CardService()
        return service.create(data)