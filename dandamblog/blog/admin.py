from django.contrib import admin
from .models import Post
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = {'content'}

admin.site.register(Post, PostAdmin)

class FlatPageAdmin(SummernoteModelAdmin):
    summernote_fields = {'content'}
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

