from django.urls import path

from card.views import CardView

app_name = 'card'


urlpatterns = [
    path('cards/<int:card_id>/', CardView.as_view(), name='card_detail'),
]