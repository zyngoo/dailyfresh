from django.contrib import admin
from models import *

# Register your models here.
class  TypeInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "ttitle"]


class GoodInfoAdmin(admin.ModelAdmin):
    list_display = ["id","gtitle","gprice","gunit","gcontent","gtype"]



admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodInfo,GoodInfoAdmin)
