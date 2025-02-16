from django.contrib import admin
from cubs.models import Page, PageManager

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

@admin.register(PageManager)
class PageManagerAdmin(admin.ModelAdmin):
    list_display = ("user", "page")

