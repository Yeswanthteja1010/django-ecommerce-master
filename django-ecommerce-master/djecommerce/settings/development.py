from .base import *
import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
    'django.contrib.admin',
    
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}
"""
DATABASES = {
    'default': {
       

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nrtech_example',
        'USER': 'postgres',
        'PASSWORD': 'Teja@1010',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}"""

import dj_database_url
DATABASES = {
    'default': dj_database_url.parse('postgresql://nrtech:TJHt0vP9x0JdfUigAm9Dq8MU4wZcFv9X@dpg-cpqnhlqj1k6c73bk1gl0-a.ohio-postgres.render.com/nrtech_example')
}

STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
