from django.contrib import admin
from .models import Places

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'text', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Places, PlacesAdmin)

