import sys
import os

# Increase the recursion limit
sys.setrecursionlimit(1500)

# Set the paths and environment variables.
# Hosting-specific paths are taken from the environment instead of being hard-coded:
#   DJANGO_PROJECT_PATH - folder that contains manage.py (default: this file's folder)
#   VENV_SITE_PACKAGES  - site-packages of the virtualenv on the server (optional)
sys.path.append(os.environ.get('DJANGO_PROJECT_PATH', os.path.dirname(os.path.abspath(__file__))))
if os.environ.get('VENV_SITE_PACKAGES'):
    sys.path.append(os.environ['VENV_SITE_PACKAGES'])
os.environ['DJANGO_SETTINGS_MODULE'] = 'grantproject.settings'

# Import the application directly from wsgi.py
try:
    from grantproject.wsgi import application
except Exception as e:
    # Log the error or print it for debugging
    print(f"Error importing application: {e}")
    raise
