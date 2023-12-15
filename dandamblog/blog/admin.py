from django.contrib import admin
# from django.contrib import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post, Category
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
# from django_summernote.admin import SummernoteModelAdmin
from unfold.admin import ModelAdmin

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'category')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    # summernote_fields = {'content'}

admin.site.register(Post, PostAdmin)

class FlatPageAdmin(FlatPageAdmin):
#     summernote_fields = {'content'}
    fieldsets = [
        (None, {'fields': ['title', 'url', 'content',]}),
        (
            _('Advanced options'),
         {
            'classes': ['collapse'],
            'fields': ['template_name','sites'],
         },
        ),
    ]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

