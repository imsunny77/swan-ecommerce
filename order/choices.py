from django.db import models

class PaymentStatus(models.IntegerChoices):
    PENDING = 0, ('PENDING')
    PAID    = 1, ('PAID')
