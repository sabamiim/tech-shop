from itertools import product

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from store.cart import Cart
from store.forms import SignUpForm
from store.models import Order, Product, OrderItem


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

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('cart_detail')

def remove_from_cart(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart_detail.html', {'cart':cart})


@login_required()
def checkout(request):
    cart = Cart(request)
    if request.method == "post":
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price'],
            )
        cart.clear()
        return redirect("profile")
    return render(request,"store/checkout.html",{"cart":cart})

@login_required
def profile(request):
    orders = request.user.orders.all()
    return render(request, "store/profile.html", {"orders": orders})





