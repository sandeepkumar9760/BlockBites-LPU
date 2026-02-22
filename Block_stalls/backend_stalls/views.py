from django.shortcuts import render , get_object_or_404 , redirect
from .models import Block , Stall , MenuItem , TimeSlot , Order ,  OrderItem 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def checkout(request):
    if request.method == "POST":
        cart = request.session.get('cart', {})
        slot_id = request.POST.get('slot')

        if not cart:
            return redirect('cart')

        time_slot = TimeSlot.objects.get(id=slot_id)

        # Get first item to determine block and stall
        first_item = MenuItem.objects.get(id=list(cart.keys())[0])
        block = first_item.stall.block
        stall = first_item.stall

        order = Order.objects.create(
            user=request.user,
            block=block,
            stall=stall,
            time_slot=time_slot,
            total_price=0
        )

        total = 0

        for item_id, quantity in cart.items():
            item = MenuItem.objects.get(id=item_id)
            subtotal = item.price * quantity
            total += subtotal

            OrderItem.objects.create(
                order=order,
                menu_item=item,
                quantity=quantity,
                subtotal=subtotal
            )

        order.total_price = total
        order.save()

        request.session['cart'] = {}

        return redirect('order_success')
    
@login_required 
def blocks(request):
    blocks = Block.objects.filter(is_active=True)
    return render(request, 'block.html', {'blocks': blocks})


@login_required
def stalls(request, block_id):
    block = get_object_or_404(Block, id=block_id)
    stalls = Stall.objects.filter(block=block, is_open=True)

    return render(request, 'stalls.html', {
        'block': block,
        'stalls': stalls
    })

@login_required
def menu(request, stall_id):
    stall = get_object_or_404(Stall, id=stall_id)
    menu_items = MenuItem.objects.filter(stall=stall, is_available=True)

    return render(request, 'menu.html', {
        'stall': stall,
        'menu_items': menu_items
    })

def add_to_cart(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(MenuItem, id=item_id)

        cart = request.session.get('cart', {})

        if str(item_id) in cart:
            cart[str(item_id)] += 1
        else:
            cart[str(item_id)] = 1

        request.session['cart'] = cart

        return redirect('cart')

@login_required
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for item_id, quantity in cart.items():
        item = MenuItem.objects.get(id=item_id)
        subtotal = item.price * quantity
        total += subtotal

        items.append({
            'item': item,
            'quantity': quantity,
            'subtotal': subtotal
        })

    time_slots = TimeSlot.objects.all()

    return render(request, 'cart.html', {
        'items': items,
        'total': total,
        'time_slots': time_slots
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("blocks")
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("login")

    return render(request, "login.html")

@login_required
def blocks(request):
    blocks = Block.objects.filter(is_active=True)
    return render(request, 'block.html', {'blocks': blocks})

def order_success(request):
    return render(request, 'success.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect("blocks")

    return render(request, "register.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def update_cart(request, item_id, action):
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        if action == "increase":
            cart[str(item_id)] += 1

        elif action == "decrease":
            cart[str(item_id)] -= 1
            if cart[str(item_id)] <= 0:
                del cart[str(item_id)]

        elif action == "remove":
            del cart[str(item_id)]

    request.session['cart'] = cart
    return redirect('cart')

@login_required
def stall_dashboard(request):
    # Get orders only for stalls owned by logged in user
    orders = Order.objects.filter(stall__owner=request.user).order_by('-created_at')

    return render(request, 'stall_dashboard.html', {
        'orders': orders
    })

@login_required
def update_order_status(request, order_id, status):
    order = Order.objects.get(id=order_id)

    # Security: Only stall owner can update
    if order.stall.owner != request.user:
        return redirect('stall_dashboard')

    order.status = status
    order.save()

    return redirect('stall_dashboard')