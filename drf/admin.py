from django.contrib import admin
from .models import Item

# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')
#     search_fields = ('name',)
#     list_filter = ('created_at',)
#     ordering = ('-created_at',)
    
admin.site.register(Item)
