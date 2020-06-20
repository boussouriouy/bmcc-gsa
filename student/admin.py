from django.contrib import admin
from .models import Member
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'term')
    list_links = ('name', )
    search_fields = ('name', 'position', 'term', 'alumni', 'major')
    list_per_page = 10
    
admin.site.register(Member, MemberAdmin)



