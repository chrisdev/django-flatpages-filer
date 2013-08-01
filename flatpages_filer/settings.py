from django.conf import settings

DEFAULT_PARSER = ["flatpages_filer.markdown_parser.parse",
                  {'extensions': ['codehilite', 'extra']}]

DEFAULT_TEMPLATE_CHOICES = [
    ('flatpages/default.html', 'Text Only', ),
]

FLATPAGES_FILER_PARSER = getattr(settings, 'FLATPAGES_FILER_PARSER',
                                 DEFAULT_PARSER)

FLATPAGES_FILER_TEMPLATE_CHOICES = getattr(
    settings,
    'FLATPAGES_FILER_TEMPLATE_CHOICES',
    DEFAULT_TEMPLATE_CHOICES
)
