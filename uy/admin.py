from django.contrib import admin
from .models import Schedule, SavedSchedule, Category

admin.site.register([Schedule, SavedSchedule, Category])
