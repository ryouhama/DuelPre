from library.card.domains.domain.card.value_object import CardId
from typing import Any, Dict, List
from library.card.domains.domain.card.domain import Card, Civilization, Civilizations


class CardFactory():
    def create(self, data: Dict[str, Any]) -> Card:
        return Card(
            id=CardId(data['id']),
            name=data['name'],
            cost=data['cost'],
            effect_document=data['effect_document'],
            picture_path=data['picture_path'],
            civilizations=CivilizationsFactory(data)
        )


class CivilizationsFactory():
    def create(self, data: Dict[str, Any]) -> Civilizations:
        civilizations_data: List[str] = data['civilizations']
        return Civilizations(
            items=[Civilization.to_domain(it) for it in civilizations_data]
        )
