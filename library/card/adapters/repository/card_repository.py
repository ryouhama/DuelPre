from library.card.domains.factory.card_factory import CardFactory
from library.card.adapters.adapter.card_adpter import CardAdapter
from library.card.applications.dto.conditions.card_conditions import CardConditions
from library.card.domains.domain.card.value_object import CardId
from library.card.domains.domain.card.domain import Card, Cards
from library.card.applications.repository_interface.card_repostiroy_interface import CardRepositoryInterface
from library.card.models.card import models


class CardRepository(CardRepositoryInterface):

    def get(self, id: CardId) -> Card:
        model_card = models.Card.objects.get(id=id.value)
        data = CardAdapter(model_card).serialize()
        return CardFactory.create(data)

    def fetch_by_condition(self, conditions: CardConditions) -> Cards:
        return super().fetch_by_condition(conditions)

    def create(self, card: Card) -> None:
        return super().create(card)