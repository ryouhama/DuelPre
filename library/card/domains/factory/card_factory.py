from typing import Any, Dict, List


from dataclasses import dataclass
from card.domains.domain.card.value_object import CardId
from card.domains.domain.card.domain import (
    Card, Civilization, Civilizations)


@dataclass(frozen=True)
class CardFactory:
    data: Dict[str, Any]

    def create(self) -> Card:
        self.is_valid()
        return Card(
            id=CardId(self.data['id']) if hasattr(self.data, 'id') else None,
            name=self.data['name'],
            cost=self.data['cost'],
            effect_document=self.data['effect_document'],
            picture_path=self.data['picture_path'],
            civilizations=CivilizationsFactory(self.data)
        )

    def is_valid(self) -> bool:
        assert hasattr(self.data, 'name')
        assert hasattr(self.data, 'cost')
        assert hasattr(self.data, 'effect_document')
        assert hasattr(self.data, 'picture_path')
        assert hasattr(self.data, 'civilizations')
        return True


@dataclass(frozen=True)
class CivilizationsFactory():
    data: Dict[str, Any]

    def create(self) -> Civilizations:
        civilizations_data: List[str] = self.data['civilizations']
        return Civilizations(
            items=[Civilization.to_domain(it) for it in civilizations_data]
        )
