from django.conf import settings

PARSER = getattr(
                settings, 'FLATPAGES_FIlER_PARSER', [
                "flatpages_filer.markdown_parser.parse",{}
                ]
    )
DEFAULT_TEMPLATE_CHOICES = [
    ('flatpages/default.html', 'Text Only', ),
]
FPX_TEMPLATE_CHOICES = getattr(
    settings, 'FLATPAGES_FILER_TEMPLATE_CHOICES', DEFAULT_TEMPLATE_CHOICES)
