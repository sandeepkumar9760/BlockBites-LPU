from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.shortcuts import render
from .models import Block , Stall , MenuItem

def blocks(request):
    blocks = Block.objects.filter(is_active=True)
    return render(request, 'block.html', {'blocks': blocks})

def stalls(request, block_id):
    block = get_object_or_404(Block, id=block_id)
    stalls = Stall.objects.filter(block=block, is_open=True)

    return render(request, 'stalls.html', {
        'block': block,
        'stalls': stalls
    })

def menu(request, stall_id):
    stall = get_object_or_404(Stall, id=stall_id)
    menu_items = MenuItem.objects.filter(stall=stall, is_available=True)

    return render(request, 'menu.html', {
        'stall': stall,
        'menu_items': menu_items
    })

def login_view(request):
    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required

@login_required
def blocks(request):
    blocks = Block.objects.filter(is_active=True)
    return render(request, 'block.html', {'blocks': blocks})