from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html');

def index_with_id(request, id):
    return render(request, 'frontend/index.html');