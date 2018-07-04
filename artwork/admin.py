from django.contrib import admin
from .models import Artpiece, webContent


class ArtpieceAdmin(admin.ModelAdmin):
    fields = ['title','image_tag', 'image', 'medium', 'create_date', 'description']
    readonly_fields = ['image_tag']



class webContentAdmin(admin.ModelAdmin):
    fields = ['propertyName', 'propertyValue']


    # obj = my model
    # ** there may or may not be multiple additional arguments


admin.site.register(Artpiece, ArtpieceAdmin,)
admin.site.register(webContent, webContentAdmin)



# Register your models here.

