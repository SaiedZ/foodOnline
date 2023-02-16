from django.shortcuts import redirect, render
from accounts.forms import UserForm


def register_user(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()

    context = {'form': form}

    return render(request, 'accounts/registerUser.html', context=context)
