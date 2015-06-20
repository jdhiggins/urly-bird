from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Click

class ClickAdmin(admin.ModelAdmin):
    list_display = ['bookmark', 'time', 'address', 'browser', 'user']

admin.site.register(Click, ClickAdmin)
