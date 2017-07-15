from django.contrib import admin
from todo.models import Task, Category, Priority

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Priority)
