import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'django')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'django.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
