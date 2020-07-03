from django.contrib import admin
from .models import user_model,ActivityPeriod
# Register your models here.

admin.site.register(user_model)

admin.site.register(ActivityPeriod)
