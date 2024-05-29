from django.shortcuts import render


def index(request):
    return render(request, '127.0.0.1.html')
