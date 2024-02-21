from django.contrib import admin
from app1.models import Movie

# Register your models here.
import django.apps

models = django.apps.apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass