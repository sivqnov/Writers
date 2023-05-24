from django.shortcuts import render
from .models import Author, Genre, Work
from django.core.paginator import Paginator
from Members.models import Profile
from django.db.models import Q
from Main.symbols import *
# Create your views here.

ITEMS_ON_PAGE = 4

def writers(request):
    authors = Author.objects.order_by('name')
    pag = Paginator(authors, ITEMS_ON_PAGE)
    page_number = request.GET.get('page', 1)
    page = pag.get_page(page_number)
    context = {
        'title': 'Пiсьменнiкi',
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
    items = Genre.objects.order_by('title')
    pag = Paginator(items, ITEMS_ON_PAGE)
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
    items = Work.objects.order_by('title')
    pag = Paginator(items, ITEMS_ON_PAGE)
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

def get_writers(request):
    array = ['name', '-name', 'date_of_birth', '-date_of_birth',]
    if request.method == "GET":
        try:
            cat = int(request.GET.get('category', 0))
        except:
            cat = 0
        if cat >= len(array) or cat < 0:
            cat=0
        q = clean_q(request.GET.get('q', '')[:MAX_QUERY_LENGTH])
        with_photo = request.GET.get('with_photo', 'off')
        with_alias = request.GET.get('with_alias', 'off')
        page_number = int(request.GET.get('page', 1))
        page_action = request.GET.get('pag', 'blin')
        if q=='':
            items = Author.objects.order_by(array[cat])
        else:
            items = Author.objects.filter(Q(name__iregex=q) | Q(alias__iregex=q) | Q(preview__iregex=q) | Q(content__iregex=q)).order_by(array[cat])
        if with_photo == 'on':
            items = items.exclude(photo='')
        if with_alias == 'on':
            items = items.exclude(alias='')
        pag = Paginator(items, ITEMS_ON_PAGE)
        page = pag.get_page(page_number)
        if page_action == 'next' and page.has_next():
            page_number += 1
        elif page_action == 'prev' and page.has_previous():
            page_number -= 1
        pag = Paginator(items, ITEMS_ON_PAGE)
        page = pag.get_page(page_number)
        context = {
            'items': page,
        }
        return render(request, 'inc/authors.html', context)

def get_genres(request):
    array = ['title', '-title',]
    if request.method == "GET":
        try:
            cat = int(request.GET.get('category', 0))
        except:
            cat = 0
        if cat >= len(array) or cat < 0:
            cat=0
        q = clean_q(request.GET.get('q', '')[:MAX_QUERY_LENGTH])
        with_photo = request.GET.get('with_photo', 'off')
        page_number = int(request.GET.get('page', 1))
        page_action = request.GET.get('pag', 'blin')
        if q=='':
            items = Genre.objects.order_by(array[cat])
        else:
            items = Genre.objects.filter(Q(title__iregex=q) | Q(preview__iregex=q) | Q(content__iregex=q)).order_by(array[cat])
        if with_photo == 'on':
            items = items.exclude(photo='')
        pag = Paginator(items, ITEMS_ON_PAGE)
        page = pag.get_page(page_number)
        if page_action == 'next' and page.has_next():
            page_number += 1
        elif page_action == 'prev' and page.has_previous():
            page_number -= 1
        pag = Paginator(items, ITEMS_ON_PAGE)
        page = pag.get_page(page_number)
        context = {
            'items': page,
        }
        return render(request, 'inc/genres.html', context)

def get_works(request):
    array = ['title', '-title',]
    if request.method == "GET":
        try:
            cat = int(request.GET.get('category', 0))
        except:
            cat = 0
        if cat >= len(array) or cat < 0:
            cat=0
        q = clean_q(request.GET.get('q', '')[:MAX_QUERY_LENGTH])
        with_photo = request.GET.get('with_photo', 'off')
        page_number = int(request.GET.get('page', 1))
        page_action = request.GET.get('pag', 'blin')
        if q=='':
            items = Work.objects.order_by(array[cat])
        else:
            items = Work.objects.filter(Q(title__iregex=q) | Q(preview__iregex=q) | Q(content__iregex=q)).order_by(array[cat])
        if with_photo == 'on':
            items = items.exclude(photo='')
        pag = Paginator(items, ITEMS_ON_PAGE)
        page = pag.get_page(page_number)
        if page_action == 'next' and page.has_next():
            page_number += 1
        elif page_action == 'prev' and page.has_previous():
            page_number -= 1
        pag = Paginator(items, ITEMS_ON_PAGE)
        page = pag.get_page(page_number)
        context = {
            'items': page,
        }
        return render(request, 'inc/works.html', context)