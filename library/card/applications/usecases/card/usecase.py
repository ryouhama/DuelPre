from typing import Any, Dict, List


from card.applications.repository_interface.card_repostiroy_interface \
    import CardRepositoryInterface
from card.domains.domain.card.value_object import CardId
from card.applications.dto.conditions.card_conditions \
    import CardConditionDto
from injector import inject


class CardUsecase():

    @inject
    def __init__(
        self,
        card_repository: CardRepositoryInterface
    ) -> None:
        self.card_repository = card_repository

    def get(self, card_id: int) -> Dict[str, Any]:
        card_id_obj = CardId(card_id)
        data = self.card_repository.get(card_id_obj)
        return data.to_dict()

    def fetch(self, input_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        dto = CardConditionDto(
            id=input_data.get('id', None),
            keyward=input_data.get('keyward', None),
            civilizations=input_data.get('civilizations', None)
        )
        data = self.card_repository.fetch_by_condition(dto)
        return [it.to_dict() for it in data.items]

    def create(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        data = self.card_repository.create(input_data)
        return {'id': data.value}

    def delete(self, card_id: int) -> Dict[str, Any]:
        card_id_obj = CardId(card_id)
        data = self.card_repository.delete(card_id_obj)
        return {'id': data.value}
