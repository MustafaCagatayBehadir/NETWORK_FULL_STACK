# This file is used as a configuration for local deployment of Netbox.

ALLOWED_HOSTS = ["*"]

DATABASE = {
    "NAME": "netbox",  # Database name
    "USER": "netbox",  # PostgreSQL username
    "PASSWORD": "netbox",  # PostgreSQL password
    "HOST": "postgres",  # Database server
    "PORT": "",  # Database port (leave blank for default)
    "CONN_MAX_AGE": 300,  # Max database connection age
}
REDIS = {
    "tasks": {
        "HOST": "redis",
        "PORT": 6379,
        # Comment out `HOST` and `PORT` lines and uncomment the following if using Redis Sentinel
        # 'SENTINELS': [('mysentinel.redis.example.com', 6379)],
        # 'SENTINEL_SERVICE': 'netbox',
        "USERNAME": "",
        "PASSWORD": "mysecretpassword",
        "DATABASE": 0,
        "SSL": False,
        # Set this to True to skip TLS certificate verification
        # This can expose the connection to attacks, be careful
        # 'INSECURE_SKIP_TLS_VERIFY': False,
        # Set a path to a certificate authority, typically used with a self signed certificate.
        # 'CA_CERT_PATH': '/etc/ssl/certs/ca.crt',
    },
    "caching": {
        "HOST": "redis-cache",
        "PORT": 6379,
        # Comment out `HOST` and `PORT` lines and uncomment the following if using Redis Sentinel
        # 'SENTINELS': [('mysentinel.redis.example.com', 6379)],
        # 'SENTINEL_SERVICE': 'netbox',
        "USERNAME": "",
        "PASSWORD": "mysecretpassword",
        "DATABASE": 1,
        "SSL": False,
        # Set this to True to skip TLS certificate verification
        # This can expose the connection to attacks, be careful
        # 'INSECURE_SKIP_TLS_VERIFY': False,
        # Set a path to a certificate authority, typically used with a self signed certificate.
        # 'CA_CERT_PATH': '/etc/ssl/certs/ca.crt',
    },
}

# Specify one or more name and email address tuples representing NetBox administrators. These people will be notified of
# application errors (assuming correct email settings are provided).
ADMINS = [
    # ('John Doe', 'jdoe@example.com'),
]

# Permit the retrieval of API tokens after their creation.
ALLOW_TOKEN_RETRIEVAL = False

# Enable any desired validators for local account passwords below. For a list of included validators, please see the
# Django documentation at https://docs.djangoproject.com/en/stable/topics/auth/passwords/#password-validation.
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #     'OPTIONS': {
    #         'min_length': 10,
    #     }
    # },
]

# Base URL path if accessing NetBox within a directory. For example, if installed at https://example.com/netbox/, set:
# BASE_PATH = 'netbox/'
BASE_PATH = ""

# API Cross-Origin Resource Sharing (CORS) settings. If CORS_ORIGIN_ALLOW_ALL is set to True, all origins will be
# allowed. Otherwise, define a list of allowed origins using either CORS_ORIGIN_WHITELIST or
# CORS_ORIGIN_REGEX_WHITELIST. For more information, see https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    # 'https://hostname.example.com',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    # r'^(https?://)?(\w+\.)?example\.com$',
]

# The name to use for the CSRF token cookie.
CSRF_COOKIE_NAME = "csrftoken"

# Set to True to enable server debugging. WARNING: Debugging introduces a substantial performance penalty and may reveal
# sensitive information about your installation. Only enable debugging while performing testing. Never enable debugging
# on a production system.
DEBUG = False

# Set the default preferred language/locale
DEFAULT_LANGUAGE = "en-us"

# Email settings
EMAIL = {
    "SERVER": "localhost",
    "PORT": 25,
    "USERNAME": "",
    "PASSWORD": "",
    "USE_SSL": False,
    "USE_TLS": False,
    "TIMEOUT": 10,  # seconds
    "FROM_EMAIL": "",
}

# Localization
ENABLE_LOCALIZATION = False

# Exempt certain models from the enforcement of view permissions. Models listed here will be viewable by all users and
# by anonymous users. List models in the form `<app>.<model>`. Add '*' to this list to exempt all models.
EXEMPT_VIEW_PERMISSIONS = [
    # 'dcim.site',
    # 'dcim.region',
    # 'ipam.prefix',
]

# HTTP proxies NetBox should use when sending outbound HTTP requests (e.g. for webhooks).
# HTTP_PROXIES = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080',
# }

# IP addresses recognized as internal to the system. The debugging toolbar will be available only to clients accessing
# NetBox from an internal IP.
INTERNAL_IPS = ("127.0.0.1", "::1")

# Enable custom logging. Please see the Django documentation for detailed guidance on configuring custom logs:
#   https://docs.djangoproject.com/en/stable/topics/logging/
LOGGING = {}

# Automatically reset the lifetime of a valid session upon each authenticated request. Enables users to remain
# authenticated to NetBox indefinitely.
LOGIN_PERSISTENCE = False

# Setting this to True will permit only authenticated users to access any part of NetBox. By default, anonymous users
# are permitted to access most data in NetBox but not make any changes.
LOGIN_REQUIRED = False

# The length of time (in seconds) for which a user will remain logged into the web UI before being prompted to
# re-authenticate. (Default: 1209600 [14 days])
LOGIN_TIMEOUT = None

# The view name or URL to which users are redirected after logging out.
LOGOUT_REDIRECT_URL = "home"

# The file path where uploaded media such as image attachments are stored. A trailing slash is not needed. Note that
# the default value of this setting is derived from the installed location.
# MEDIA_ROOT = '/opt/netbox/netbox/media'

# Expose Prometheus monitoring metrics at the HTTP endpoint '/metrics'
METRICS_ENABLED = False

# Enable installed plugins. Add the name of each plugin to the list.
PLUGINS = []

# Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
# PLUGINS_CONFIG = {
#     'my_plugin': {
#         'foo': 'bar',
#         'buzz': 'bazz'
#     }
# }

# Remote authentication support
REMOTE_AUTH_ENABLED = False
REMOTE_AUTH_BACKEND = "netbox.authentication.RemoteUserBackend"
REMOTE_AUTH_HEADER = "HTTP_REMOTE_USER"
REMOTE_AUTH_AUTO_CREATE_USER = True
REMOTE_AUTH_DEFAULT_GROUPS = []
REMOTE_AUTH_DEFAULT_PERMISSIONS = {}

# This repository is used to check whether there is a new release of NetBox available. Set to None to disable the
# version check or use the URL below to check for release in the official NetBox repository.
RELEASE_CHECK_URL = None
# RELEASE_CHECK_URL = 'https://api.github.com/repos/netbox-community/netbox/releases'

# The file path where custom reports will be stored. A trailing slash is not needed. Note that the default value of
# this setting is derived from the installed location.
# REPORTS_ROOT = '/opt/netbox/netbox/reports'

# Maximum execution time for background tasks, in seconds.
RQ_DEFAULT_TIMEOUT = 300

# The file path where custom scripts will be stored. A trailing slash is not needed. Note that the default value of
# this setting is derived from the installed location.
# SCRIPTS_ROOT = '/opt/netbox/netbox/scripts'

# The name to use for the session cookie.
SESSION_COOKIE_NAME = "sessionid"

# By default, NetBox will store session data in the database. Alternatively, a file path can be specified here to use
# local file storage instead. (This can be useful for enabling authentication on a standby instance with read-only
# database access.) Note that the user as which NetBox runs must have read and write permissions to this path.
SESSION_FILE_PATH = None

# By default, uploaded media is stored on the local filesystem. Using Django-storages is also supported. Provide the
# class path of the storage driver in STORAGE_BACKEND and any configuration options in STORAGE_CONFIG. For example:
# STORAGE_BACKEND = 'storages.backends.s3boto3.S3Boto3Storage'
# STORAGE_CONFIG = {
#     'AWS_ACCESS_KEY_ID': 'Key ID',
#     'AWS_SECRET_ACCESS_KEY': 'Secret',
#     'AWS_STORAGE_BUCKET_NAME': 'netbox',
#     'AWS_S3_REGION_NAME': 'eu-west-1',
# }

# Time zone (default: UTC)
TIME_ZONE = "UTC"

# Date/time formatting. See the following link for supported formats:
# https://docs.djangoproject.com/en/stable/ref/templates/builtins/#date
DATE_FORMAT = "N j, Y"
SHORT_DATE_FORMAT = "Y-m-d"
TIME_FORMAT = "g:i a"
SHORT_TIME_FORMAT = "H:i:s"
DATETIME_FORMAT = "N j, Y g:i a"
SHORT_DATETIME_FORMAT = "Y-m-d H:i"
DEVELOPER = True

# SECRET_KEY = "+hxYOo+U-u0)1%rlzSrXU7YFH^9JHYWIDf)aQTrvc7x0$SDjJE"
