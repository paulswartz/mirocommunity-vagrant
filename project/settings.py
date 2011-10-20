# Django settings for project project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'miro_community',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/vagrant/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6&@xpf%$%5nsz5bq7-*x@e2=@oujh1#jc*v64meosc26m%8ktx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'uploadtemplate.loader.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'localtv.middleware.FixAJAXMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'openid_consumer.middleware.OpenIDMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'localtv.middleware.UserIsAdminMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".  Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'localtv.playlists',
    'django.contrib.comments',
    'openid_consumer',
    'voting',
    'localtv.user_profile',
    'localtv.search',
    'tagging',
    'email_share',
    'django.contrib.flatpages',
    'localtv.inline_edit',
    'localtv.submit_video',
    'notification',
    'registration',
    'paypal.standard.ipn',
    'localtv.admin',
    'djpagetabs',
    'djvideo',
    'socialauth',
    'celery',
    'haystack',
    'south',
    'localtv',
    'uploadtemplate',
    'localtv.comments',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "localtv.context_processors.localtv")

FORCE_SCRIPT_NAME = ''

LOGIN_PAGE = LOGIN_REDIRECT_URL = '/'
OPENID_REDIRECT_TO = '/accounts/openid/complete/'
OPENID_REDIRECT_NEXT = '/accounts/openid/done/'

OPENID_SREG = {"requred": "nickname, email, fullname",
               "policy_url": ""}

#example should be something more like the real thing, i think
OPENID_AX = [{"type_uri": "http://axschema.org/contact/email",
              "count": 1,
              "required": True,
              "alias": "email"},
             {"type_uri": "http://axschema.org/schema/fullname",
              "count":1 ,
              "required": False,
              "alias": "fname"}]

OPENID_AX_PROVIDER_MAP = {
    'Google': {'email': 'http://axschema.org/contact/email',
               'firstname': 'http://axschema.org/namePerson/first',
               'lastname': 'http://axschema.org/namePerson/last'},
    'Default': {'email': 'http://axschema.org/contact/email',
                'fullname': 'http://axschema.org/namePerson',
                'nickname': 'http://axschema.org/namePerson/friendly'}
    }

AUTHENTICATION_BACKENDS = (
    'localtv.backend.SiteAdminBackend',
    'socialauth.auth_backends.TwitterBackend',
    'socialauth.auth_backends.FacebookBackend',
    'socialauth.auth_backends.OpenIdBackend',
	)

DEFAULT_FROM_EMAIL = 'Miro Community <mirocommunity@pculture.org>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

GOOGLE_ANALYTICS_UA = "UA-163840-18"
GOOGLE_ANALYTICS_DOMAIN = "mirocommunity.org"

AUTH_PROFILE_MODULE = 'user_profile.Profile'

CACHE_BACKEND = 'locmem://' #'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

COMMENTS_APP = 'localtv.comments'

ACCOUNT_ACTIVATION_DAYS = 7

UPLOADTEMPLATE_STATIC_ROOTS = ['/home/vagrant/src/miro-community/static']
UPLOADTEMPLATE_TEMPLATE_ROOTS = [
    '/home/vagrant/src/miro-community/localtv/templates']

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

MEDIA_URL = '/media/'

UPLOADTEMPLATE_MEDIA_ROOT = '/vagrant/virtualenv/src/localtv-themes/'
UPLOADTEMPLATE_MEDIA_URL = '/media/uploadtemplate'
def UPLOADTEMPLATE_DISABLE_UPLOAD():
    localtv = __import__('localtv.models')
    tier = localtv.models.SiteLocation.objects.get_current().get_tier()
    return not tier.enforce_permit_custom_template()

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'project.search_sites'
HAYSTACK_WHOOSH_PATH = '/home/vagrant/whoosh_index/'

BROKER_HOST = 'localhost'
BROKER_PORT = 5672
BROKER_USER = 'guest'
BROKER_PASSWORD = 'guest'
BROKER_VHOST = '/'
CELERY_BACKEND = 'database'
CELERY_RESULT_DBURI = 'mysql://root@localhost/miro_community'
CELERYD_CONCURRENCY = 1
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_LEVEL = 'INFO'

FORCE_LOWERCASE_TAGS = True

PAGETABS_END_SIZE = 1

FACEBOOK_APP_ID = None
FACEBOOK_API_KEY = None
FACEBOOK_SECRET_KEY = None
FACEBOOK_CONNECT_URL = ('http://www-dev.mirocommunity.org/facebook/'
                        'connect/?next=%s')
FACEBOOK_CONNECT_DOMAIN = 'mirocommunity.org'

TWITTER_CONSUMER_KEY = None
TWITTER_CONSUMER_SECRET = None
TWITTER_ACCESS_TOKEN = None
TWITTER_ACCESS_TOKEN_SECRET = None

BITLY_LOGIN = None
BITLY_API_KEY = None

RECAPTCHA_PUBLIC_KEY = None
RECAPTCHA_PRIVATE_KEY = None

VIMEO_API_KEY = None
VIMEO_API_SECRET = None

USTREAM_API_KEY = None

from secrets import *

FLOWPLAYER_SWF_URL='/swf/flowplayer.swf'
FLOWPLAYER_CONTROLS_URL='/swf/flowplayer.controls.swf'
FLOWPLAYER_JS_URL='/js/extern/flowplayer.min.js'

### Payment-related settings
# Use the "live" PayPal processing service, not the "sandbox".
PAYPAL_TEST=True
# Configure the site to send money to this email address
PAYPAL_RECEIVER_EMAIL="donate@pculture.org"

### ZenDesk settings, related to tiers
LOCALTV_USE_ZENDESK=False

## Enable "stamps" that indicate to our management command wrapper scripts if a
## video has been modified since the last time we ran the managment commands.
LOCALTV_ENABLE_CHANGE_STAMPS = True

VOTING_ENABLED = True
