from django.shortcuts import render, redirect
from account.models import Account, KYC
from account.forms import KYCForm
from django.contrib import messages

# Create your views here.

def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user = user)

    try:
        kyc = KYC.objects.get(user = user)
    except KYC.DoesNotExist:
        kyc = None
    

    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, 'KYC form submitted successfully, In review now')
            return redirect("core:index")
    
    form = KYCForm(instance=kyc)
    context = {
            'account': account,
            'form': form,
            'kyc':kyc
        }
    return render(request, 'account/kyc-form.html', context)


# *1. def kyc_registration(request):*
# - Defines a view function named kyc_registration that takes a request object as an argument.

# *2. user = request.user*
# - Retrieves the currently logged-in user from the request object.

# *3. account = Account.objects.get(user=user)*
# - Retrieves the user's account instance from the database using the Account model.

# *4. try: kyc = KYC.objects.get(user=user)*
# - Tries to retrieve an existing KYC (Know Your Customer) instance for the user from the database using the KYC model.

# *5. except KYC.DoesNotExist: kyc = None*
# - If no KYC instance exists for the user, sets kyc to None.

# *6. if request.method == 'POST':*
# - Checks if the request method is POST (i.e., the form has been submitted).

# *7. print(request.POST)*
# - Prints the POST data (form data) for debugging purposes.

# *8. print(request.FILES)*
# - Prints the uploaded files (if any) for debugging purposes.

# *9. form = KYCForm(request.POST, request.FILES, instance=kyc)*
# - Creates a new KYCForm instance with the submitted data and files, and associates it with the existing KYC instance (if any).

# *10. if form.is_valid():*
# - Checks if the form data is valid.

# *11. new_form = form.save(commit=False)*
# - Saves the form data to a new KYC instance without committing it to the database yet.

# *12. new_form.user = user*
# - Sets the user attribute of the new KYC instance to the current user.

# *13. new_form.account = account*
# - Sets the account attribute of the new KYC instance to the user's account.

# *14. new_form.save()*
# - Saves the new KYC instance to the database.

# *15. messages.success(request, 'KYC form submitted successfully, In review now')*
# - Displays a success message to the user.

# *16. return redirect("core:index")*
# - Redirects the user to the core:index URL.

# *17. form = KYCForm(instance=kyc)*
# - Creates a new KYCForm instance with the existing KYC data (if any).

# *18. context = {'account': account, 'form': form, 'kyc': kyc}*
# - Creates a context dictionary with the account, form, and KYC data.

# *19. return render(request, 'account/kyc-form.html', context)*

# - Renders the kyc-form.html template with the context data.
