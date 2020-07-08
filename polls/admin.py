from django.contrib import admin
from polls import models


admin.site.register(models.Question)
admin.site.register(models.Choice)
admin.site.register(models.Employer)
admin.site.register(models.Departments)
admin.site.register(models.Tea)

