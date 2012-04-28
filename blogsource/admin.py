from django.contrib import admin
from blogsource.models import Blog, Category, Comment, Image, Link

class InlineImage(admin.TabularInline):
    model = Image

class InlineLink(admin.TabularInline):
    model = Link

class BlogAdmin(admin.ModelAdmin):
    # exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [InlineImage, InlineLink]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
