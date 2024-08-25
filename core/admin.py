from django.contrib import admin
from core.models import Transaction

# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_editable = [ 'amount', 'sender', 'receiver', 'transaction_status', 'transaction_type' ]
    list_display = ['user', 'amount', 'sender', 'receiver', 'transaction_type', 'transaction_status' ]
admin.site.register(Transaction, TransactionAdmin)