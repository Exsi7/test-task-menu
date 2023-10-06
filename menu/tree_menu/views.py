from django.shortcuts import render
from menu.tree_menu.models import Menu

# Create your views here.
def index(request):
    return render(request, "index.html")


def tree_view(request, url):
    return render(request, "index.html")