import os
import sys
 
# Hosting-specific paths come from the environment (see .env.example)
sys.path.append(os.environ.get('DJANGO_PROJECT_PATH', os.path.dirname(os.path.abspath(__file__))))
if os.environ.get('VENV_SITE_PACKAGES'):
    sys.path.append(os.environ['VENV_SITE_PACKAGES'])
os.environ['DJANGO_SETTINGS_MODULE'] = 'grantproject.settings'
import django
django.setup()
 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()