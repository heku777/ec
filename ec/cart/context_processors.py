from .models import Cart, CartItem
from .views import _user_id


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            _cart_user_id = Cart.objects.filter(user_id=_user_id(request))
            cart_items = CartItem.objects.all().filter(
                cart_user_id=_cart_user_id[:1])
            for cart_item in cart_items:
                item_count += cart_item.product_number
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
