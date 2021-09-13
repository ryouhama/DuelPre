from django.contrib import admin
from card.models.card import models


admin.site.register(models.Card)
admin.site.register(models.CardCivilization)
admin.site.register(models.Civilization)
