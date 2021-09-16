from abc import ABC, abstractclassmethod, abstractmethod


from card.domains.domain.card.value_object import CardId
from card.applications.dto.conditions.card_conditions \
    import CardConditionDto
from card.domains.domain.card.domain import Card, Cards


class CardRepositoryInterface(ABC):
    """
    CardRepositoryのInterfaceクラス
    カードのデータ操作の関数をもつ
    """

    @abstractmethod
    def get(self, id: CardId) -> Card:
        """
        カードIDに応じたカードデータを1件取得する
        """
        raise NotImplementedError()

    @abstractclassmethod
    def fetch_by_condition(self, dto: CardConditionDto) -> Cards:
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

    @abstractclassmethod
    def delete(self, card_id: CardId) -> CardId:
        """
        カードデータを削除する
        """
        raise NotImplementedError()
