from django.contrib import admin
from Job.models import *
# Register your models here.

@admin.register(Job_Post)
class JobDataAdmin(admin.ModelAdmin):
    list_display = ['company','job_title', 'position', 'status']
    
