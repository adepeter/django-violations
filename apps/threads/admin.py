from django.contrib import admin

from .models import Thread

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'starter', 'text']