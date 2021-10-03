from django.shortcuts import render


def main(request):
    return render(request, 'djangoProject/index.html')


def contacts(request):
    return render(request, 'djangoProject/contact.html')
