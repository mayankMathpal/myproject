from typing import Tuple

from django.contrib import admin
from django.utils.html import format_html

from .models import Profile,Address
# Register your models here.
class aminok(admin.ModelAdmin):

    def image(self, obj):
        return format_html('<img src="{}" width = "40px"/>'.format(obj.profilePic.url))
    image.short_description = 'image'

    list_display = ('name','image','phoneNo','genderField','dob')
    list_filter = ('genderField','perma_address__city')
    search_fields = ('name',)
    fields = ('image_profile','name','phoneNo','genderField', 'profilePic', 'dob', 'perma_address', 'company_address', 'friends')
    lst = ['image_profile']

    readonly_fields = ('image_profile',)

class address(admin.ModelAdmin):
    list_display = ('city','pincode','state')

admin.site.register(Profile, aminok)
admin.site.register( Address, address )
