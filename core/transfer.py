from account.models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from account.models import Account, KYC
from django.contrib import messages
from django.db.models import Q

# 1302327510470
@login_required
def search_user_by_account_number(request):
    #account = Account.objects.filter(account_status = 'active')
    accounts = Account.objects.all()

    search_query = request.POST.get("account_number") 
    
    if search_query:
        accounts = accounts.filter(
            Q(account_number=search_query)|
            Q(account_id = search_query)
        ).distinct


    context = {
        'accounts': accounts,
        'search_query': search_query
    }
    return render(request, 'transfer/search-user-by-account-number.html', context)


def amount_transfer(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number)
        
    except:
        messages.warning(request, "Account does not exist.")
        return redirect('core:search-account')

    context = {
        'account':account
    }
    return render(request, "transfer/amount_transfer.html", context)
