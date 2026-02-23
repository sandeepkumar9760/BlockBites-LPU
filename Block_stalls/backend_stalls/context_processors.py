def cart_count(request):
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())
    return {'cart_count': total_items}

from .models import Order

def notification_count(request):
    if request.user.is_authenticated:
        count = Order.objects.filter(
            user=request.user,
            status="Confirmed",
            is_seen=False
        ).count()
        return {"global_notifications": count}
    return {}