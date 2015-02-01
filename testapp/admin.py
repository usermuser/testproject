from django.contrib import admin

# Register your models here.

from testapp.models import Poll,Choice


admin.site.register(Poll)
admin.site.register(Choice)
