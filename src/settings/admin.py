from django.contrib import admin
from django.contrib.admin.decorators import register
from settings.models import Brand,Variant

admin.site.register(Brand)
admin.site.register(Variant)