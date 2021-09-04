from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CardConditionDto():
    """
    カードデータの検索条件
    """
    id: Optional[int]
    keyward: Optional[str]
    civilizations: Optional[List[str]]
