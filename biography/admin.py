from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from .forms import *

class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'folder', 'order')
    prepopulated_fields = {'slug': ('title', )}
    list_editable = ('order', )
    ordering = ('order',)

class SkillAdmin(admin.ModelAdmin):
    fields = ('name', 'icon', 'get_html_photo', 'cat', 'icon_svg', 'get_svg_icon', 'background', 'is_filter')
    readonly_fields = ('get_html_photo', 'get_svg_icon')
    list_filter = ('cat', 'is_filter')
    list_display = ('name', 'cat', 'get_html_photo', 'get_svg_icon', 'is_filter')
    search_fields = ('name',)

    def get_svg_icon(self, obj):
        if obj.icon_svg:
            return mark_safe(f'<div style="width: 20px; height: 20px;">{obj.icon_svg}</div>')
        return "-"

    def get_html_photo(self, object):
         if(object.icon):
            return mark_safe(f'<img src="{object.get_icon_url}" alt="" width=20>')
         
    get_html_photo.short_description = 'Miniature'
    get_svg_icon.short_description = 'SVG Icon'

class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'icon_svg', 'get_svg_icon', 'url', 'order')
    readonly_fields = ('get_svg_icon',)
    list_display = ('name', 'get_svg_icon', 'order')
    list_editable = ('order', )
    ordering = ('order', )

    def get_svg_icon(self, obj):
        if obj.icon_svg:
            return mark_safe(f'<div style="width: 20px; height: 20px;">{obj.icon_svg}</div>')
        return "-"
    
    get_svg_icon.short_description = 'SVG Icon'

class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'name')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'subname', 'time_start', 'time_end')

# Register your models here.
admin.site.register(SkillCategory)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(FolderModel)
admin.site.register(FileModel, FileAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(PrimaryBio)
admin.site.register(Contact, ContactAdmin)