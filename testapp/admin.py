from django.contrib import admin

# Register your models here.

from testapp.models import Poll

admin.site.register(Poll)