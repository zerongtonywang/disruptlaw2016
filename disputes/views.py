from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html', {})

def resolve(request):
    return render(request, 'resolve.html', {})

def dispute(request):
    return render(request, 'dispute.html', {})