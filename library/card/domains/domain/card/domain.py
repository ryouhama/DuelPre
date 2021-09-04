from __future__ import annotations
from dataclasses import dataclass
from library.card.domains.domain.card.value_object import CardId
from library.card.domains.exception import DomainNotCreatedException
from typing import Dict, List
from enum import Enum


@dataclass
class Cards():
    """
    カードの複数ドメイン
    """
    items: List[Card]

@dataclass
class Card():
    """
    カードデータ
    """
    id: CardId
    name: str
    cost: int
    effect_document: str
    picture_path: str
    civilizations: Civilizations


@dataclass
class Civilizations():
    """
    文明の複数ドメイン
    """
    items: List[Civilization]

    def sort(self):
        self.items.sort(key=lambda it: it.value[1])

    def to_dict(self) -> Dict[str, str]:
        self.sort()
        return {
            'civilizations': [it.name for it in self.items]
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

    @classmethod
    def to_domain(cls, args_name: str) -> Civilization:
        """
        引数(args_name)で指定された文明のドメインのオブジェクトを返す
        指定された文明が存在しない場合、例外を上げる
        """
        if args_name == cls.fire.name:
            return Civilization[cls.fire]
        elif args_name == cls.water.name:
            return Civilization[cls.water]
        elif args_name == cls.natural.name:
            return Civilization[cls.natural]
        elif args_name == cls.light.name:
            return Civilization[cls.light]
        elif args_name == cls.darkness.name:
            return Civilization[cls.darkness]
        else:
            DomainNotCreatedException(
                domain=cls, message=f'文明は存在しません args={args_name}'
            )
        