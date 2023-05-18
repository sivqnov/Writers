from django.contrib import admin
from .models import Author, Genre, Work, AuthorComment, GenreComment, WorkComment
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'alias', 'name')
    list_display_links = ('id', 'alias', 'name')
    search_fields = ('id', 'alias', 'name', 'preview', 'content')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'preview', 'content')
    list_filter = ['id', 'title']

class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title', 'preview', 'content')

class AuthorCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'user', 'content')
    list_display_links = ('id', 'author', 'user', 'content')
    search_fields = ('id', 'author', 'user', 'content')

class GenreCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'user', 'content')
    list_display_links = ('id', 'author', 'user', 'content')
    search_fields = ('id', 'author', 'user', 'content')

class WorkCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'user', 'content')
    list_display_links = ('id', 'author', 'user', 'content')
    search_fields = ('id', 'author', 'user', 'content')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(AuthorComment, AuthorCommentAdmin)
admin.site.register(GenreComment, GenreCommentAdmin)
admin.site.register(WorkComment, WorkCommentAdmin)