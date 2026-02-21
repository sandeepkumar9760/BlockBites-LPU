from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Block

def blocks(request):
    blocks = Block.objects.filter(is_active=True)
    return render(request, 'block.html', {'blocks': blocks})