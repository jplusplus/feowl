#!/usr/bin/env python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'django')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'django.settings'

from django.contrib.auth.models import User
u, created = User.objects.get_or_create(username='admin')
if created:
    u.set_password('password')
    u.is_superuser = True
    u.is_staff = True
    u.save()
