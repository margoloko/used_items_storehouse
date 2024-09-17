from django.contrib import admin
from django.contrib.admin import register

from .models import (Item, Buyer, Objects)


@register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    list_filter = ('full_name', )
    save_on_top = True
    search_fields = ('full_name',)
    ordering = ('full_name', )
    empty_value_display = "-отсутствуют-"


@register(Objects)
class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', )
    save_on_top = True
    search_fields = ('name',)
    ordering = ('name', )
    empty_value_display = "-отсутствуют-"


@register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', "amount", "measurement_unit", "aim",)
    list_filter = ('name', "amount", "measurement_unit", "aim",)
    save_on_top = True
    search_fields = ('name', "amount", "measurement_unit", "aim", )
    ordering = ('name', "amount", "measurement_unit", "aim",)
    empty_value_display = "-отсутствуют-"