from django.contrib import admin

from .models import Photo,  Profile

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 3



class ProfileAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    

admin.site.register(Profile, ProfileAdmin)


