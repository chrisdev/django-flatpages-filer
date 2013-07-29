from django.conf import settings

default_parser = ["flatpages_filer.markdown_parser.parse",
                  {'extensions': ['codehilite', 'extras']}]

PARSER = getattr(settings, 'FLATPAGES_FIlER_PARSER', default_parser)

DEFAULT_TEMPLATE_CHOICES = [
    ('flatpages/default.html', 'Text Only', ),
]

FPX_TEMPLATE_CHOICES = getattr(
    settings, 'FLATPAGES_FILER_TEMPLATE_CHOICES', DEFAULT_TEMPLATE_CHOICES)
