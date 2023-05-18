from django.shortcuts import render
from .models import Author, Genre, Work
from django.core.paginator import Paginator
# Create your views here.

def writers(request):
    authors = Author.objects.order_by('-id')
    items_on_page = 6
    pag = Paginator(authors, items_on_page)
    page_number = request.GET.get('page', 1)
    page = pag.get_page(page_number)
    context = {
        'title': 'Писатели',
        'items': page,
    }
    return render(request, 'writers.html', context)

def view_author(request, author_id):
    author = Author.objects.get(id=author_id)
    works = Work.objects.filter(authors__id = author_id)
    context = {
        'title': author.name,
        'author': author,
        'works': works,
    }
    return render(request, 'author.html', context)

def genres(request):
    items = Genre.objects.order_by('-id')
    items_on_page = 6
    pag = Paginator(items, items_on_page)
    page_number = request.GET.get('page', 1)
    page = pag.get_page(page_number)
    context = {
        'title': 'Жанры',
        'items': page,
    }
    return render(request, 'genres.html', context)

def view_genre(request, genre_id):
    item = Genre.objects.get(id=genre_id)
    context = {
        'title': item.title,
        'item': item,
    }
    return render(request, 'genre.html', context)

def works(request):
    items = Work.objects.order_by('-id')
    items_on_page = 6
    pag = Paginator(items, items_on_page)
    page_number = request.GET.get('page', 1)
    page = pag.get_page(page_number)
    context = {
        'title': 'Работы',
        'items': page,
    }
    return render(request, 'works.html', context)

def view_work(request, work_id):
    item = Work.objects.get(id=work_id)
    context = {
        'title': item.title,
        'item': item,
    }
    return render(request, 'work.html', context)