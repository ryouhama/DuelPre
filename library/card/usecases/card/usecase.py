from card.services.card.service import CardService


class CardUsecase:

    def get(self, card_id: int):
        service = CardService()
        return service.get(card_id) if service.exists(card_id) else {}