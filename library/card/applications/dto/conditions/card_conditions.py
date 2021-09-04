from dataclasses import dataclass

from django.db.models.query_utils import Q
from typing import Any, Dict, List, Optional


@dataclass
class CardCondition():
    """
    カードデータの検索条件
    """
    id: Optional[int]
    keyward: Optional[str]
    civilizations: Optional[List[str]]

    def to_dict(self) -> Dict[str, Any]:
        """
        存在する条件のみのDictを作成する
        """
        base_dit = {}
        if self.id:
            base_dit['id'] = self.id
        if self.keyward:
            base_dit['keyward'] = self.keyward
        if self.civilizations:
            base_dit['civilizations'] = [it for it in self.civilizations]
        return base_dit

    def to_condition(self) -> Q:
        conditions = None
        if self.id:
            conditions = Q(id=self.id)
        if self.keyward:
            self.__add_conditions(
                prev=conditions,
                add=Q(name_startwith=self.keyward)
            )
        if self.civilizations:
            values = [it for it in self.civilizations]
            add_condition = Q(civilization__civilizations__name_in=values)
            self.__add_conditions(
                prev=conditions,
                add=add_condition
            )
        return conditions if conditions else Q()

    def __add_conditions(self, prev: Optional[Q], add: Q) -> Q:
        return Q(prev, add) if prev else add
