from django.contrib import admin
from novels.models import Post


# Register your models here.blogpost
class Postadmin(admin.ModelAdmin):
    list_display = ['title','slug','intro','body','date_created']


admin.site.register(Post,Postadmin)