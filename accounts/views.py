from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib import messages

from accounts.forms import UserForm

User = get_user_model()


def register_user(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'Your account have been created successfully')
            return redirect('register_user')
    else:
        form = UserForm()

    context = {'form': form}

    return render(request, 'accounts/registerUser.html', context=context)
