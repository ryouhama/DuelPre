from typing import Any, Dict


from card.applications.repository_interface.card_repostiroy_interface \
    import CardRepositoryInterface
from card.applications.usecases.card.usecase import CardUsecase
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from django.db import transaction
from injector import Binder, Injector, Module
from card.adapters.repository.card_repository import CardRepository


class CardFetchView(APIView):
    """
    カード一覧取得View
    """
    usecase: CardUsecase

    class InjectConfig(Module):
        def configure(self, binder: Binder) -> None:
            binder.bind(CardRepositoryInterface, to=CardRepository)

    def __init__(self, **kwargs: Any) -> None:
        injector = Injector(self.InjectConfig())
        self.usecase = injector.get(CardUsecase)
        super().__init__(**kwargs)

    def get(self, request: Request, fomat=None):
        """
        カードデータを一覧取得する
        """
        card_usecase = CardUsecase()
        data = card_usecase.fetch(request.data)
        return Response(data=data, status=status.HTTP_200_OK)


class CardView(APIView):
    """
    カードView
    """
    permission_classes = [AllowAny]
    usecase: CardUsecase

    class InjectConfig(Module):
        def configure(self, binder: Binder) -> None:
            binder.bind(CardRepositoryInterface, to=CardRepository)

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        injector = Injector(self.InjectConfig())
        self.usecase = injector.get(CardUsecase)
        super().__init__(**kwargs)

    def get(self, request: Request, card_id: int, format=None):
        """
        カードデータを1件取得する
        """
        data = self.usecase.get(card_id)
        return Response(data=data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: Request, format=None):
        """
        カードデータを作成する
        """
        data = self.usecase.get(request.data)
        return Response(data=data, status=status.HTTP_201_CREATED)
