#coding: utf-8

from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Service, Offer

class OfferInline(admin.TabularInline):
    model = Offer
    extra = 1

class ServiceAdmin(admin.ModelAdmin):
    inlines = [OfferInline]

class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'service')
    list_filter = ('service',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'service':
            kwargs['queryset'] = Service.objects.filter()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Offer, OfferAdmin)
