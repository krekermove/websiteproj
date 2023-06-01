from django.contrib import admin
from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'text', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tasks, TasksAdmin)

