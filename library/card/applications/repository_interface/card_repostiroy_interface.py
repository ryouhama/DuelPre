from abc import ABC, abstractclassmethod, abstractmethod
from card.domains.domain.card.value_object import CardId
from card.applications.dto.conditions.card_conditions \
    import CardCondition
from card.domains.domain.card.domain import Card, Cards


class CardRepositoryInterface(ABC):

    @abstractmethod
    def get(self, id: CardId) -> Card:
        """
        カードIDに応じたカードデータを1件取得する
        """
        raise NotImplementedError()

    @abstractclassmethod
    def fetch_by_condition(self, condition: CardCondition) -> Cards:
        """
        検索条件に応じてカードデータを取得する
        """
        raise NotImplementedError()

    @abstractclassmethod
    def create(self, card: Card) -> Card:
        """
        カードデータを作成する
        """
        raise NotImplementedError()
