from abc import ABC, abstractclassmethod, abstractmethod
from library.card.domains.domain.card.value_object import CardId
from library.card.applications.dto.conditions.card_conditions import CardConditions
from library.card.domains.domain.card.domain import Card, Cards

class CardRepositoryInterface(ABC):

    @abstractmethod
    def get(self, id: CardId) -> Card:
        """
        カードIDに応じたカードデータを1件取得する
        """
        raise NotImplementedError()

    @abstractclassmethod
    def fetch_by_condition(self, conditions: CardConditions) -> Cards:
        """
        検索条件に応じてカードデータを取得する
        """
        raise NotImplementedError()

    @abstractclassmethod
    def create(self, card: Card) -> None:
        """
        カードデータを作成する
        """
        raise NotImplementedError()