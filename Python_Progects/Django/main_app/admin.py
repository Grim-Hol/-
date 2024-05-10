from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author','status', 'data_reverse')
    list_display_links = ('id','title')
    search_fields = ('title','author')

admin.site.register(Articles,ArticlesAdmin)

