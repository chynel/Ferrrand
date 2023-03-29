#coding: utf-8

from django.contrib.auth.models import Permission

service_perms = [
    Permission.objects.get(codename='add_service'),
    Permission.objects.get(codename='change_service'),
    Permission.objects.get(codename='delete_service'),
    Permission.objects.get(codename='view_service'),
]

offer_perms = [
    Permission.objects.get(codename='add_offer'),
    Permission.objects.get(codename='change_offer'),
    Permission.objects.get(codename='delete_offer'),
    Permission.objects.get(codename='view_offer'),
]

superuser_perms = service_perms + offer_perms