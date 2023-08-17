from django.contrib import admin

from .models import Tag, Organization, Job
# Register your models here.

admin.site.register(Tag)
admin.site.register(Organization)
admin.site.register(Job)
