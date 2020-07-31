from django.contrib import admin
from .models import Books

admin.site.register(Books)

admin.site.site_header = "Geektext Admin"
admin.site.site_title = "Geektext Admin Area"
admin.site.index_header = "Welcome to the Geektext Admin Area"