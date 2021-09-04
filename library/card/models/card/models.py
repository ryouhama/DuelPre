from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from card.models.foundation.models import CommonModel


class Card(CommonModel):
    class Meta:
        db_table = 'カード'

    name = models.CharField(max_length=200)
    cost = models.IntegerField()
    effect_document = models.CharField(max_length=1000)
    picture_path = models.CharField(max_length=200)

    @property
    def civilizations(self):
        return self.civilization.civilizations.all()

class CardCivilization(CommonModel):
    class Meta:
        db_table = 'カード-文明'

    card = models.OneToOneField('Card',on_delete=models.CASCADE, related_name='civilization')
    civilizations = models.ForeignKey('Civilization', on_delete=models.CASCADE, related_name='cards')

class Civilization(CommonModel):
    class Meta:
        db_table = '文明'

    CIVILIZATION_TYPES = (
      ('fire', '火'),
      ('water', '水'),
      ('natural', '自然'),
      ('light', '光'),
      ('darkness', '闇')
    )

    name = models.CharField(choices=CIVILIZATION_TYPES, max_length=8)
