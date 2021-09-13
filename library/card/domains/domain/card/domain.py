from __future__ import annotations
from dataclasses import dataclass
from card.domains.domain.card.value_object import CardId
from typing import Any, Dict, List, Optional
from enum import Enum


@dataclass
class Cards():
    """
    AggregateCard
    """
    items: List[Card]


@dataclass
class Card():
    """
    カードデータ
    """
    id: Optional[CardId]
    name: str
    cost: int
    effect_document: str
    picture_path: str
    civilizations: Civilizations

    def to_dict(self) -> Dict[str, Any]:
        data = {
            'id': self.id.value if self.id else None,
            'name': self.name,
            'cost': self.cost,
            'effect_document': self.effect_document,
            'picture_path': self.picture_path
        }
        data.update(self.civilizations.to_dict())
        return data


@dataclass
class Civilizations():
    """
    AggregateCivilization
    """
    items: List[Civilization]

    def sort(self):
        self.items.sort(key=lambda it: it.value[1])

    def to_dict(self) -> Dict[str, str]:
        self.sort()
        return {
            'civilizations': [it.label() for it in self.items]
        }


@dataclass
class Civilization(Enum):
    """
    文明
    """
    fire = ('火文明', 1)
    water = ('水文明', 2)
    natural = ('自然文明', 3)
    light = ('光文明', 4)
    darkness = ('闇文明', 5)

    def label(self) -> str:
        return self.value[0]

    @classmethod
    def to_domain(cls, args_name: str) -> Civilization:
        """
        引数(args_name)で指定された文明のドメインのオブジェクトを返す
        指定された文明が存在しない場合、例外を上げる
        """
        if args_name == cls.fire.name:
            return Civilization(cls.fire)
        elif args_name == cls.water.name:
            return Civilization(cls.water)
        elif args_name == cls.natural.name:
            return Civilization(cls.natural)
        elif args_name == cls.light.name:
            return Civilization(cls.light)
        elif args_name == cls.darkness.name:
            return Civilization(cls.darkness)
        else:
            raise Exception(f'Civilization not exist: args={args_name}')
