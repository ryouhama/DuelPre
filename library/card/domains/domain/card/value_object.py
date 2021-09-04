from dataclasses import dataclass


@dataclass(frozen=True)
class CardId():
    """
    カードID
    """
    value: int
