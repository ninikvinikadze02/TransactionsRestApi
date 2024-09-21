from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_id', 'user_id', 'transaction_time', 'item_code', 'item_description', 'quantity_items',
                  'item_cost', 'country')
