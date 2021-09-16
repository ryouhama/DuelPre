from django.urls import path


from card.applications.views import card_view

app_name = 'card'


urlpatterns = [
    path('cards/', card_view.CardFetchView.as_view(), name='card_list'),
    path(
        'cards/create/',
        card_view.CardView.as_view(),
        name='card_detail_create'
    ),
    path(
        'cards/<int:card_id>/',
        card_view.CardView.as_view(),
        name='card_detail'
    )
]
