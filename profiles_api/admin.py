from django.contrib import admin

# Register your models here.
from . import models

# admin.site.register(models.Demo)
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
