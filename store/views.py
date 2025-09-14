from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from store.forms import SignUpForm
from store.models import Order


def signup_view(request):
    if request == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
        else:
            form = SignUpForm
            return render(request,'store/signup.html', {'form' : form})


@login_required
def profile_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/profile,html', {'orders':orders})

