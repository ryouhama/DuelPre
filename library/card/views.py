from card.usecases.card.usecase import CardUsecase
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from django.db import transaction


class CardFetchView(APIView):
    """
    カード一覧取得View
    """

    def get(self, request: Request, fomat=None):
        """
        カードデータを一覧取得する
        """
        card_usecase = CardUsecase()
        data = card_usecase.fetch()
        return Response(data=data, status=status.HTTP_200_OK)


class CardView(APIView):
    """
    カードView
    """
    permission_classes = [AllowAny]

    def get(self, request: Request, card_id: int, format=None):
        """
        カードデータを1件取得する
        """
        card_usecase = CardUsecase()
        data = card_usecase.get(card_id)
        return Response(data=data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: Request, format=None):
        """
        カードデータを作成する
        """
        card_usecase = CardUsecase()
        data = card_usecase.create(request.data)
        return Response(data=data, status=status.HTTP_201_CREATED)
