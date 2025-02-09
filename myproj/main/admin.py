from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import book
from .models import teacher,test

admin.site.register(book)
admin.site.register(teacher)
admin.site.register(test)