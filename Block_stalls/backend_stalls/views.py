from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.shortcuts import render
from .models import Block , Stall

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

def login_view(request):
    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required

@login_required
def blocks(request):
    blocks = Block.objects.filter(is_active=True)
    return render(request, 'block.html', {'blocks': blocks})