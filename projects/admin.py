from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'excerpt')
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Redirect)
admin.site.register(Contributor)