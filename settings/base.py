# -*- coding: utf-8 -*-
import os

# 
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__))).replace("\\", "/")

# Default: () (Empty tuple) a;slkdal;ksdl;aks;dlakl;sdkl;aks;dlkal;sdkl;askdl;akd
# A tuple that lists people who get code error notifications.
# When DEBUG=False and a view raises an exception,# Django will e-mail these
# people with the full exception information.
# Each member of the tuple should be a tuple of (Full name, e-mail address).
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

# Default: () (Empty tuple)
# A tuple in the same format as ADMINS that specifies who should get broken-link
# notifications when SEND_BROKEN_LINK_EMAILS=True.
MANAGERS = ADMINS

# Default: 'America/Chicago'
# A string representing the time zone for this installation, or None.
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# (Note that list of available choices lists more than one on the same line;
# you'll want to use just one of the choices for a given time zone.
# For instance, one line says 'Europe/London GB GB-Eire', but you should use the
# first bit of that -- 'Europe/London' -- as your TIME_ZONE setting.)
TIME_ZONE = 'America/Chicago'

# Default: 'en-us'
# A string representing the language code for this installation. This should be in
# standard language format. For example, U.S. English is "en-us".
# http://docs.djangoproject.com/en/1.2/topics/i18n/#topics-i18n
LANGUAGE_CODE = 'en-us'

# Default: Not defined
# The ID, as an integer, of the current site in the django_site database table.
# This is used so that application data can hook into specific site(s) and a single
# database can manage content for multiple sites.
# http://docs.djangoproject.com/en/1.2/ref/contrib/sites/#ref-contrib-sites
SITE_ID = 1

# Default: True
# A boolean that specifies whether Django's internationalization system should be
# enabled. This provides an easy way to turn it off, for performance. If this is
# set to False, Django will make some optimizations so as not to load the
# internationalization machinery.
USE_I18N = True

# Default False
# A boolean that specifies if data will be localized by default or not.
# If this is set to True, e.g. Django will display numbers and dates using the
# format of the current locale.
USE_L10N = True

# Default: '' (Empty string)
# Absolute path to the directory that holds media for this installation.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# Default: '' (Empty string)
# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
# Note that this should have a trailing slash if it has a path component.
# Good: "http://www.example.com/static/" Bad: "http://www.example.com/static"
MEDIA_URL = ''

# Default: '/media/'
# The URL prefix for admin media -- CSS, JavaScript and images used by the Django
# administrative interface. Make sure to use a trailing slash, and to have this be
# different from the MEDIA_URL setting (since the same URL cannot be mapped onto
# two different sets of files).
ADMIN_MEDIA_PREFIX = '/media/'

# Default: '' (Empty string)
# A secret key for this particular Django installation. Used to provide a seed in
# secret-key hashing algorithms. Set this to a random string -- the longer, the better. 
SECRET_KEY = ''

#Default:
#('django.template.loaders.filesystem.Loader',
# 'django.template.loaders.app_directories.Loader')
# A tuple of template loader classes, specified as strings. Each Loader class
# knows how to import templates from a particular source. Optionally, a tuple
# can be used instead of a string. The first item in the tuple should be the
# Loader's module, subsequent items are passed to the Loader during initialization.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates")
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # admin backend
    'django.contrib.admin',
    'django.contrib.admindocs',
    # included for all projects and environments
    'django_extensions',
    'south',
)
