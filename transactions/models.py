from django.db import models


class Transaction(models.Model):
    transaction_id = models.IntegerField()
    user_id = models.IntegerField()
    transaction_time = models.DateTimeField()
    item_code = models.CharField(max_length=50)
    item_description = models.CharField(max_length=5000)
    quantity_items = models.IntegerField()
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user_id} - {self.item_code}"
