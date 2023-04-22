from django.shortcuts import render

# Create your views here.

def main(request):
    context = {
        'title': 'Галоўная старонка',
    }
    return render(request, 'main.html', context)

def about(request):
    context = {
        'title': 'Аб сайце',
    }
    return render(request, 'about.html', context)