from django.contrib import admin
from .models import Category, Article, ArticleImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleImage)
