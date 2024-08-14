from account.models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from account.models import Account, KYC
from django.contrib import messages
from django.db.models import Q
from core.models import Transaction

# 1302327510470
@login_required
def search_user_by_account_number(request):
    #account = Account.objects.filter(account_status = 'active')
    accounts = Account.objects.all()

    search_query = request.POST.get("account_number") # Shows the profile of the intended recipient, corresponding to the account number entered by the current user, to ensure accurate and secure fund transfers
    
    if search_query:
        accounts = accounts.filter( # Successfully retrieves  the accurate account information of the intended recipient, ensuring a precise match based on the entered account number.
            Q(account_number=search_query)|  # Q is used when you need to filter a queryset based on multiple conditions, or when you need to use logical operators
            Q(account_id = search_query)
        ).distinct


    context = {
        'accounts': accounts, # this shows the infomation(only basic basic info like profilepic, name and account.no are displyed to user) of the indended recipient based on the entered account number.
        'search_query': search_query
    }
    return render(request, 'transfer/search-user-by-account-number.html', context)


def amount_transfer(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number) # After verifying the intended recipient's account information( from def search_user_by_account_number), the user confirms the transaction by sending the payee's account number through a secure URL(refer core/urls.py eg:path("amount-transfer/<account_number>/", transfer.amount_transfer) which then redirects them to the next page. The system holds the transaction details of payee until the transfer is fully completed, note: this account is payee's. 
        
    except:
        messages.warning(request, "Account does not exist.")# if enterd a wrong account number
        return redirect('core:search-account')

    context = {
        'account':account
    }
    return render(request, "transfer/amount_transfer.html", context)

def AmountTransferProcess(request, account_number):
    receiver_account = Account.objects.get(account_number=account_number) # we can retrieve an Account object using any of the unique fields in the model
    sender_account = request.user.account 
    # example of reverse relation(note:giving a related name while creating db will increase readability.)
    sender = request.user 
    receiver = receiver_account.user 

    if request.method == "POST":
        amount = request.POST.get("amount_sent")
        description = request.POST.get("description")

        print(amount)
        print(description)

        if sender_account.account_balance > 0 and amount:  # creates and keep track of the transaction made my user succesfully.
            new_transaction = Transaction.objects.create(
            user = request.user,
            amount = amount,
            description = description,
            receiver = receiver,
            sender = sender,
            sender_account = sender_account,
            receiver_account = receiver_account,
            transaction_status = "Proccessing",
            transaction_type = "transfer"
        )
            new_transaction.save()
            transaction_id = new_transaction.transaction_id #"The transaction ID will be generated automatically, as specified in the models.py file. Once the transaction is complete, the ID will be provided.
            return redirect("core:transfer-confirmation", receiver_account.account_number, transaction_id)
        else:
             messages.warning(request,"Insufficient fund")
             return redirect("core:amount-transfer", receiver_account.account_number)
    else:
         messages.warning(request,"error occured try again")
         return redirect("account:account")

def TransferConfirmation(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning(request, "transaction does not exist")
        return redirect('core:search-account')

    context = {
        'account': account,
        'transaction': transaction
    }
    return render(request, "transfer/transfer-confirmation.html", context)
    

    