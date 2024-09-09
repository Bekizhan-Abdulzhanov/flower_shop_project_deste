from django.contrib import admin

from apps.flowers.models import Flower,FlowerImage

class FlowerInLine(admin.TabularInline):
    model = FlowerImage
    extra = 1

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    inlines = [FlowerInLine]

@admin.register(FlowerImage)
class FlowerImageAdmin(admin.ModelAdmin):
    list_display = ['image']