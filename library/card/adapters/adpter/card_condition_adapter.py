from dataclasses import dataclass
from typing import Optional
from django.db.models.query_utils import Q
from card.applications.dto.conditions.card_conditions \
    import CardConditionDto


@dataclass
class CardConditionAdapter():
    dto: CardConditionDto

    def to_query_condition(self) -> Q:
        conditions = Q()

        if self.dto.id:
            self.__add_conditions(
                prev=conditions,
                add=Q(id=self.dto.id)
            )

        if self.dto.keyward:
            self.__add_conditions(
                prev=conditions,
                add=Q(name_startwith=self.dto.keyward)
            )

        if self.dto.civilizations:
            values = [it for it in self.dto.civilizations]
            add_condition = Q(civilization__civilizations__name_in=values)
            self.__add_conditions(
                prev=conditions,
                add=add_condition
            )

        return conditions

    def __add_conditions(self, prev: Optional[Q], add: Q) -> Q:
        """
        prev条件に、ANDでadd条件を追加する
        """
        return Q(prev, add) if prev else add
