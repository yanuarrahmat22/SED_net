from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request, 'index.php')


