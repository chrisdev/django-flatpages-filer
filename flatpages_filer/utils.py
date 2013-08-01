from django.core.exceptions import ImproperlyConfigured
from .settings import DEFAULT_PARSER, DEFAULT_TEMPLATE_CHOICES
from django.conf import settings
try:
    from django.utils.importlib import import_module
except ImportError:
    from importlib import import_module


def get_template_choices():
    return getattr(settings, 'FLATPAGES_FILER_TEMPLATE_CHOICES',
                   DEFAULT_TEMPLATE_CHOICES)


def get_parser():
    return getattr(settings, 'FLATPAGES_FILER_PARSER', DEFAULT_PARSER)


def load_path_attr(path):
    i = path.rfind(".")
    module, attr = path[:i], path[i + 1:]
    try:
        mod = import_module(module)
    except ImportError, e:
        raise ImproperlyConfigured("Error importing %s: '%s'" % (module, e))
    try:
        attr = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured(
            "Module '%s' does not define a '%s'" % (module, attr))
    return attr
