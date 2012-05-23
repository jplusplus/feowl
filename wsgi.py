import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'django')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'django.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
