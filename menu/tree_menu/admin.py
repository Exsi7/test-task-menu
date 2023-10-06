from django.contrib import admin
from menu.tree_menu.models import Menu, MenuItem
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    search_fields = ['name']


admin.site.register(Menu, MenuAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'menu', 'url', 'parent']
    search_fields = ['name', 'menu']


admin.site.register(MenuItem, MenuItemAdmin)
