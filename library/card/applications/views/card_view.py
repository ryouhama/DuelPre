from typing import Any, Dict


from card.applications.repository_interface.card_repostiroy_interface \
    import CardRepositoryInterface
from card.applications.usecases.card.usecase import CardUsecase
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from django.db import transaction
from injector import Binder, Injector, Module
from card.adapters.repository.card_repository import CardRepository


class CardListView(APIView):
    """
    カード一覧取得View

    get:
    一覧取得
    リクエストのパラメータによって取得条件を得る

    post:
    カード作成
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
        data = self.usecase.fetch(request.data)
        return Response(data=data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: Request, format=None):
        """
        カードデータを作成する
        """
        data = self.usecase.create(request.data)
        return Response(data=data, status=status.HTTP_201_CREATED)


class CardView(APIView):
    """
    カードView

    get:
    カード1件取得

    delete:
    カード削除
    """
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
    def delete(self, request: Request, card_id: int, format=None):
        """
        カードデータを削除する
        """
        data = self.usecase.delete(card_id)
        return Response(data=data, status=status.HTTP_202_ACCEPTED)
