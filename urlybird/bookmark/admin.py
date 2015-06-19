from django.contrib import admin

# Register your models here.
from .models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['user', 'long', 'short', 'title', 'description', 'created', 'edited']

admin.site.register(Bookmark, BookmarkAdmin)