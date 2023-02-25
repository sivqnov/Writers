from django.shortcuts import render

# Create your views here.

def mainPage(request):
    context = {
        'title': 'Писатели Беларуси',
        'request': request,
    }
    return render(request, 'mainPage/mainPage.html', context)