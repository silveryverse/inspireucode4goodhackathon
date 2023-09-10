from django.contrib import admin
from service.models import UploadedImage

class serviceAdmin(admin.ModelAdmin):
    list_display=('image','location','pincode','description','uploaded_at')


# Register your models here.
admin.site.register(UploadedImage,serviceAdmin)
