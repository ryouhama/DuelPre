from django.urls import path

from card import views

app_name = 'card'


urlpatterns = [
    path('cards/', views.CardFetchView.as_view(), name='card_list'),
    path('cards/<int:card_id>/', views.CardView.as_view(), name='card_detail'),
    path('cards/', views.CardView.as_view(), name='card_detail_create')
]
