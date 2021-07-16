from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import User
from .models import Author, Contact


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']
admin.site.register(Author, AuthorAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'message']
admin.site.register(Contact, ContactAdmin)
