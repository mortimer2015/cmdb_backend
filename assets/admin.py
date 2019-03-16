from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Assets)
admin.site.register(models.AssetType)
admin.site.register(models.Groups)

