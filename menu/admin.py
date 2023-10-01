from django.contrib import admin
from .models import Items

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('dish', 'status')
    list_filter = ('status', )   #tuple
    search_fields = ('dish', 'description')

admin.site.register(Items, MenuItemAdmin)