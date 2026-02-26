import os
from django.core.wsgi import get_wsgi_application

# Indicamos que use el archivo de settings de la carpeta core
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()