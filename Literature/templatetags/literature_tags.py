from django import template
from Literature.models import Author, Genre, Work

register = template.Library()

@register.inclusion_tag('modules/mini_posts.html')
def mini_posts(is_rand, type):
    type = str(type)
    amount = 4
    sort = '?' if is_rand == True else '-id'
    items = Author.objects.order_by(sort) if type == '0' else Genre.objects.order_by(sort) if type == '1' else Work.objects.order_by(sort) # 0 - Author; 1 - Genre; 2 - Work.
    context = {
        'title': 'Пiсьменнiкi' if type == '0' else 'Жанры' if type == '1' else 'Работы',
        'items': items[:amount],
        'type': type,
    }
    return context

# mini posts
# post list