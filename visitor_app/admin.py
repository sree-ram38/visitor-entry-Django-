from django.contrib import admin
from .models import EntryPass

admin.site.register(EntryPass)

# Register your models here.
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'place', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'place')
    ordering = ('created_at',)