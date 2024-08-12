from django.urls import path 
from core import views, transfer

app_name = "core"

urlpatterns = [
    path("", views.sample, name="index"),
    # transfers
    path("search-account/", transfer.search_user_by_account_number, name="search-account"),
    path("amount-transfer/<account_number>/", transfer.amount_transfer, name="amount-transfer")
]