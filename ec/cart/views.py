from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from django.views import generic
from shop.models import ShopItem
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404


def _user_id(request):
    cart_user = request.user
    print(cart_user.id)
    return cart_user.id


def add_cart(request, product_id):
    product = ShopItem.objects.get(id=product_id)
    try:
        _cart_user_id = Cart.objects.get(user_id=_user_id(request))
    except Cart.DoesNotExist:
        _cart_user_id = Cart.objects.create(
            user_id=_user_id(request)
        )
        _cart_user_id.save()
    try:
        cart_item = CartItem.objects.get(product=product,
                                         cart_user_id=_cart_user_id)
        cart_item.product_number += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            cart_user=_cart_user_id,
            product=product,
            product_number=1,
        )
        cart_item.save()
    return redirect('cart:cart_list')


def cart_list(request, total=0, counter=0, cart_items=None):
    try:
        _cart_user_id = Cart.objects.get(user_id=_user_id(request))
        cart_items = CartItem.objects.filter(cart_user_id=_cart_user_id)
        for cart_item in cart_items:
            total += int((cart_item.product.price * 1.08) * cart_item.product_number)
            counter += cart_item.product_number
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart/cart_list.html',
                  dict(cart_items=cart_items, total=total, counter=counter))


def cart_remove(request, product_id):
    _cart_user_id = Cart.objects.get(user_id=_user_id(request))
    product = get_object_or_404(ShopItem, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart_user_id=_cart_user_id)
    if cart_item.product_number > 1:
        cart_item.product_number -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_list')


def full_remove(request, product_id):
    _cart_user_id = Cart.objects.get(user_id=_user_id(request))
    product = get_object_or_404(ShopItem, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart_user_id=_cart_user_id)
    cart_item.delete()
    return redirect('cart:cart_list')
