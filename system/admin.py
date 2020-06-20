from django.contrib import admin
from .models import Event, Document
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', )
    search_fields = ('title', 'date')
    list_per_page = 5
    
admin.site.register(Event, EventAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    search_fields = ('title', )
    list_per_page = 5
    
admin.site.register(Document, DocumentAdmin)    


