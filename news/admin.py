from django.contrib import admin
from .models import Article, Editor, Tag

class ArticleAdmin(admin.ModelAdmin):
  filter_horizontal=('tags',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)