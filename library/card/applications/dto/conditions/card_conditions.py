from dataclasses import dataclass
from library.card.domains.domain.card.value_object import CardId
from library.card.domains.domain.card.domain import Civilizations
from typing import Any, Dict, Optional

@dataclass
class CardConditions():
    """
    カードデータの検索条件
    """
    id: Optional[CardId]
    keyward: Optional[str]
    civilizations: Civilizations

    def to_dict(self) -> Dict[str, Any]:
        """
        存在する条件のみのDictを作成する
        """
        base_dit = {}
        if self.id:
            base_dit['id'] = self.id.value
        if self.keyward:
            base_dit['keyward'] = self.keyward
        if self.civilizations.items:
            base_dit += self.civilizations.to_dict()
        return base_dit