from django.contrib import admin
from .models import Category, Comment, Post, Suggestions
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'category_list', 'slug', 'status', 'author', 'created_on', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('categories', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}  
    summernote_fields = ('content',)

    @admin.display(description='categories')
    def category_list(self, post):
        return ', '.join(category.name for category in post.categories.all())

    class Media:
        css = {'all': ('css/admin_comments.css',)}
        js = ('js/admin_comments.js',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'approved', 'created_on')
    list_filter = ('post__title', 'author', 'approved', 'created_on')

    class Media:
        css = {'all': ('css/admin_comments.css',)}
        js = ('js/admin_comments.js',)


@admin.register(Suggestions)
class SuggestionsAdmin(SummernoteModelAdmin):
    list_display = ('post', 'submitted_by', 'status', 'created_on', 'updated_on')
    list_filter = ('status', 'created_on')
    search_fields = ('post__title', 'submitted_by__username', 'proposed_content')
    summernote_fields = ('proposed_content',)