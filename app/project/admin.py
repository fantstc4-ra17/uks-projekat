from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(ProjectAdmin, self).get_changeform_initial_data(request)
        get_data['owner'] = request.user.pk
        return get_data

admin.site.register(Project, admin_class=ProjectAdmin)