from card.usecases.card.usecase import CardUsecase
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.request import Request

class CardView(APIView):
    """
    カードView
    """

    def get(self, request: Request, card_id: int, format=None):
        """
        カードデータを1件取得する
        """
        card_usecase = CardUsecase()
        data = card_usecase.get(card_id)
        return Response(data=data, status=HTTP_200_OK)