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
            id=CardId(self.data['id']) if self.data.get('id', None) else None,
            name=self.data['name'],
            cost=self.data['cost'],
            effect_document=self.data['effect_document'],
            picture_path=self.data['picture_path'],
            civilizations=CivilizationsFactory(self.data).create()
        )

    def is_valid(self) -> bool:
        required_set = {
            'name',
            'cost',
            'effect_document',
            'picture_path',
            'civilizations'
        }
        result = required_set == required_set & {it for it in self.data.keys()}
        if not result:
            raise Exception('Validate error: object=Card')
        return True


@dataclass(frozen=True)
class CivilizationsFactory():
    data: Dict[str, Any]

    def create(self) -> Civilizations:
        civilizations_data: List[str] = self.data['civilizations']
        return Civilizations(
            items=[
                Civilization.to_domain(it['name'])
                for it in civilizations_data
            ]
        )
