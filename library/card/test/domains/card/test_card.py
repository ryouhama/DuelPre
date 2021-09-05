import pytest
import random
import copy

from card.domains.domain.card.value_object import CardId
from card.domains.domain.card.domain import (
    Card, Civilization, Civilizations
)


class TestCard():
    def test__to_dict__ドメイン通りにDictデータが生成されていること(self):
        # Arrage
        card = Card(
            id=CardId(1),
            name='テスト',
            cost=1,
            effect_document='テスト効果',
            picture_path='/test.png',
            civilizations=Civilizations(
                [Civilization(('火文明', 1))]
            )
        )

        # Act
        actual = card.to_dict()

        # Assert
        excpected = {
            'id': 1,
            'name': 'テスト',
            'cost': 1,
            'effect_document': 'テスト効果',
            'picture_path': '/test.png',
            'civilizations': ['火文明']
        }

        assert actual == excpected


class TestCivilizations():

    def setUp(self):
        self.data = [
            ('火文明', 1),
            ('水文明', 2),
            ('自然文明', 3),
            ('光文明', 4),
            ('闇文明', 5)
        ]

    def test__sort__昇順になっていること(self):
        # Arrange
        self.setUp()
        deep_copied_data = copy.deepcopy(self.data)
        random.shuffle(deep_copied_data)
        actual = Civilizations([Civilization(it) for it in deep_copied_data])

        # Act
        actual.sort()

        # Assert
        excpected = [Civilization(it) for it in self.data]

        assert actual.items == excpected

    def test__to_dict__ドメイン通りにDictデータが生成されていること(self):
        # Arrange
        self.setUp()
        civilizations = Civilizations([Civilization(it) for it in self.data])

        # Act
        actual = civilizations.to_dict()

        # Assert
        expected = {
            'civilizations': [
                '火文明', '水文明', '自然文明', '光文明', '闇文明'
            ]
        }

        assert actual == expected


class TestCivilization():

    def test__to_domain__指定したオブジェクトが生成されていること(self):
        # Act
        actual = Civilization.to_domain('火文明')

        # Assert
        expected = Civilization(('火文明', 1))
        assert actual == expected

    def test__to_domain__存在しない文明の場合例外がスローされていること(self):
        # Act
        with pytest.raises(Exception) as error:
            Civilization.to_domain('ほげほげ')

        # Assert
        expected = 'Civilization not exist: args=ほげほげ'
        assert str(error.value) == expected
