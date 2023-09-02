from django.contrib import admin
from .models import CallsModel


# admin.site.register(Cars)
@admin.register(CallsModel)
class TestAdmin(admin.ModelAdmin):
    readonly_fields = ['time']
