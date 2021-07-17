from django.contrib import admin
from .models import Team
from .models import Contactus
from django.utils.html import format_html
# Register your models here.

#This class is used to customize the admin page of Team model
class TeamAdmin(admin.ModelAdmin):

    #This function is to show photo of team members in list on admin page of Team model
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ['id', 'first_name','thumbnail' , 'designation','created_date']
    list_display_links = ['id','first_name','thumbnail']
    search_fields = ['fist_name','last_name','designation']
    list_filter = ['designation']


admin.site.register(Team,TeamAdmin)
admin.site.register(Contactus)