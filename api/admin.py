from django.contrib import admin

# Register your models here.
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('project_name', 'start_date', 'end_date', 'status')
	list_filter = ('start_date', 'end_date', 'status', )
	search_fields = ['project_name']

admin.site.register(Project, ProjectAdmin)
