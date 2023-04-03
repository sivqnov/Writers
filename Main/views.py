from django.shortcuts import render

# Create your views here.

def main(request):
    context = {
        'title': 'Mainpage',
    }
    return render(request, 'main.html', context)