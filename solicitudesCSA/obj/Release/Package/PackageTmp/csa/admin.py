from django.contrib import admin

from csa.models import workRequest


@admin.register(workRequest)
class workRequest(admin.ModelAdmin):
    pass
