from django.conf import settings

try:
    from constance import config

    def get_settings(x):
        return getattr(config, x) if hasattr(config, x) else getattr(settings, x)
except ImportError:
    def get_settings(x):
        return getattr(settings, x)
