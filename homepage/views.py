from django.shortcuts import render
from .models import Name

# Create your views here.

def index_view(request):
    return render (request, 'index.html', {'data': Name.objects.all()})
