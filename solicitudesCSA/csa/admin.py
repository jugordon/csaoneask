from django.contrib import admin

from csa.models import CSAuser,workRequest

@admin.register(CSAuser)
class CSAuser(admin.ModelAdmin):
    pass

@admin.register(workRequest)
class workRequest(admin.ModelAdmin):
    pass
