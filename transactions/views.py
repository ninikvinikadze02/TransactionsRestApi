from rest_framework import viewsets, generics, status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.functions import TruncDate


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2500
    page_size_query_param = 'page_size'
    max_page_size = 100


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = StandardResultsSetPagination
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if not response.data:
            return Response({"detail": "No transactions available."}, status=status.HTTP_404_NOT_FOUND)
        return response


# Aggregated user purchases

class UserPurchasesView(APIView):
    http_method_names = ['get']

    def get(self, request, user_id):
        if not str(user_id).isdigit() or int(user_id) < 0:
            return Response({"detail": "Invalid user ID."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            purchases = (Transaction.objects
                         .filter(user_id=int(user_id))
                         .values('transaction_time__date')
                         .annotate(total_items=Sum('quantity_items')))

            if not purchases:
                return Response({"detail": "No purchases found for this user."}, status=status.HTTP_404_NOT_FOUND)

            return Response(purchases)
        except Exception as e:
            return Response({"detail": "An error occurred while fetching data."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductPurchasesView(APIView):
    http_method_names = ['get']

    def get(self, request, item_code):
        if not isinstance(item_code, str) or not item_code.strip():
            return Response({"detail": "Invalid item code."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            purchases = (Transaction.objects
                         .filter(item_code=item_code)
                         .values('transaction_time__date')
                         .annotate(total_items=Sum('quantity_items')))

            if not purchases:
                return Response({"detail": "No purchases found for this item."}, status=status.HTTP_404_NOT_FOUND)

            return Response(purchases)
        except Exception as e:
            return Response({"detail": "An error occurred while fetching data."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
