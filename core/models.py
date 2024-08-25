from django.db import models
from userauths.models import User
from account.models import Account
from shortuuid.django_fields import ShortUUIDField

TRANSACTION_TYPE = (
    ("transfer","transfer"),
    ("received","received"),
    ("refund","refund"),
    ("withdraw","withdraw"),
    ("request","request"),
    ("none","none")
)

TRANSACTION_STATUS = (
    ("failed","failed"),
    ("completed","completed"),
    ("failed","failed"),
    ("pending","pending"),
    ("processing","processing"),
    ("requested","requested"),
    ("request_processing","request_processing"),
    ("request_rejected","request_rejected"),
    ("request_sent","request_sent"),
    ("request settled", "request settled"),
    ("none","none")
)


# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user")
    transaction_id = ShortUUIDField(unique=True, length=15, max_length=20, prefix="TRN")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="receiver")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender")

    receiver_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="receiver_account")
    sender_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,  related_name="sender_account")   

    transaction_status = models.CharField(choices=TRANSACTION_STATUS, max_length=100, default="pending") 
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=100, default="none") 
    
    description = models.CharField(max_length=5000, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        try:
            return f"{self.user}"
        except:
            return f"Transaction"
