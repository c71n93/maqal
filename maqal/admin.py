"""Admin management for maqal application."""
from django.contrib import admin
from .models import Proverb

admin.site.register(Proverb)
