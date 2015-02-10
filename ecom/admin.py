from django.contrib import admin

# Register your models here.

from ecom.models import Catalog,Product 

admin.site.register(Catalog)
admin.site.register(Product)
