from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.transaction_type}: {self.amount} on {self.date}"

