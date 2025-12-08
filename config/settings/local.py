from .settings import *

DEBUG = True
SHELL_PLUS = "ipython"

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:5173'
]


REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'apps.core.exceptions.handler.custom_exception_handler',

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # You can also keep session auth if you use the browsable API:
        # 'rest_framework.authentication.SessionAuthentication',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',   # default: all APIs need login
    ],
}


from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

