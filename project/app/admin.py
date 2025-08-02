from django.contrib import admin

# Register your models here.
from .models import Jobs
from django.contrib.auth.models import User

class Jobadmin(admin.ModelAdmin):
    list=['id','jobtitle','description','salary','link']
admin.site.register(Jobs,Jobadmin)