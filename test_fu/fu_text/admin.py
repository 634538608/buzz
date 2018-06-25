from django.contrib import admin
from fu_text.models import GoodsInfo
# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(GoodsInfo,GoodsInfoAdmin)