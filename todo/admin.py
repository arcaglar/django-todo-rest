from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):  # add this
      list_display = ('title', 'description', 'completed')

admin.site.register(Todo, TodoAdmin)

# Register your models here.
