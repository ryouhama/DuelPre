from card.domains.factory.card_factory import CardFactory
from card.applications.dto.conditions.card_conditions \
    import CardCondition
from card.domains.domain.card.value_object import CardId
from card.domains.domain.card.domain import Card, Cards
from card.applications.repository_interface.card_repostiroy_interface \
    import CardRepositoryInterface
from card.models.card import models
from card.serializers.card.serializer import (
    CardCivilizationSerializer,
    CardFetchSerializer,
    CardSerializer
)


class CardRepository(CardRepositoryInterface):

    def get(self, id: CardId) -> Card:
        model_card = models.Card.objects.get(id=id.value)
        data = CardSerializer(model_card, patial=True).data
        return CardFactory().create(data)

    def fetch_by_condition(self, conditions: CardCondition) -> Cards:
        model_data = models.Card.objects.filter(
            conditions.to_condition()
        )
        related_model_data = CardFetchSerializer.eager_load(model_data)
        data = CardFetchSerializer(related_model_data, many=True).data
        return Cards(
            [CardFactory().create(it) for it in data]
        )

    def create(self, card: Card) -> None:
        card_data = card.to_dict()
        card_data.pop('id', None)

        civilizations_data = card_data.pop('civilizations')

        # カードデータを新規作成する
        card_serializer = CardSerializer(data=card_data, partial=True)
        if card_serializer.is_valid():
            created_card = card_serializer.save()
        else:
            raise Exception(card_serializer.errors)

        # カード-文明のリレーション関係を新規作成する
        civilization_model_data = models.Civilization.objects.filter(
            name_in=civilizations_data
        )
        for civilization in civilization_model_data:
            card_civilization_serializer = CardCivilizationSerializer(
                data={
                    'card': created_card,
                    'civilizations': civilization
                },
                partial=True
            )
            if card_civilization_serializer.is_valid():
                card_civilization_serializer.save()
            else:
                raise Exception(card_civilization_serializer.errors)

        return self.get(CardId(created_card.pk))
