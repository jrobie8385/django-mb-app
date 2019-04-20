"""
WSGI config for mb_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mb_project.settings')
#https://stackoverflow.com/questions/47616586/gunicorn-django-importerror-no-module-named-application-wsgi
#NOTE: Must put "mb_project.mb_project.settings" above since we created a django project with the extra subfolder.

application = get_wsgi_application()
