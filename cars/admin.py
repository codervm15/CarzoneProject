from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'

    list_display = ['id','car_title','thumbnail','city','color','model','year','body_style','fuel_type','is_featured']
    list_display_links = ['id', 'car_title', 'thumbnail']
    list_filter = ['car_title','city','fuel_type']
    search_fields = ['car_title','city','model','body_type']
    list_editable = ['is_featured']



admin.site.register(Car,CarAdmin)