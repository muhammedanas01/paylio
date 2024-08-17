from django.urls import path 
from core import views, transfer

app_name = "core"

urlpatterns = [
    path("", views.sample, name="index"),
    # transfers
    path("search-account/", transfer.search_user_by_account_number, name="search-account"),
    path("amount-transfer/<account_number>/", transfer.amount_transfer, name="amount-transfer"),
    path("amount-transfer-process/<account_number>/", transfer.AmountTransferProcess, name="amount-transfer-process"),
    path("transfer-confirmation/<account_number>/<transaction_id>/", transfer.TransferConfirmation, name="transfer-confirmation"),
    path("transfer-process/<account_number>/<transaction_id>/", transfer.transfer_process, name="transfer-process"),
    path("transfer-completed/<account_number>/<transaction_id>/", transfer.transfer_completed, name="transfer-completed"),

]