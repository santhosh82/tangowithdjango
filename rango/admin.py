from django.contrib import admin
from rango.models import  Category, Pages, UserProfile

# Register your models here.


admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title',  'category' , 'url')

admin.site.register(Pages, PageAdmin)


admin.site.register(UserProfile)