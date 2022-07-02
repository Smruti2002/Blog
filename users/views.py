from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account hasb been created! You are now able to Log In')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid() :
            u_form.save()
            # p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }

    return render(request,'users/profile.html', context)

