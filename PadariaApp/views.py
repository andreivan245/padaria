from django.shortcuts import render
from .models import produto

def index(request):
    produtos = produto.objects.all()
    return render(request, "PadariaApp/home.html", {"produtos": produtos})