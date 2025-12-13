REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'core.exceptions.handler.custom_exception_handler',

    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    #     # You can also keep session auth if you use the browsable API:
    #     # 'rest_framework.authentication.SessionAuthentication',
    # ],

    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',   # default: all APIs need login
    # ],
}