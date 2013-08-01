from django import forms
from django.contrib.flatpages.admin import FlatpageForm
from django.utils.translation import ugettext_lazy as _
from .utils import get_parser, get_template_choices
from .utils import load_path_attr
from .models import Revision
from datetime import datetime
try:
    from markitup.widgets import AdminMarkItUpWidget as content_widget
except ImportError:
    content_widget = forms.Textarea


class CustomFlatPageForm(FlatpageForm):
    template_name = forms.ChoiceField(
        choices=get_template_choices(), required=False,
        label='Template',
        help_text=_("Sepcify a template for displaying your content")
    )

    content_md = forms.CharField(label="Content", widget=content_widget())
    content = forms.CharField(widget=forms.Textarea(), required=False)

    def __init__(self, *args, **kwargs):

        super(CustomFlatPageForm, self).__init__(*args, **kwargs)
        fp = self.instance

        try:
            latest_revision = fp.revisions.order_by("-updated")[0]
        except IndexError:
            latest_revision = None

        if latest_revision:
            self.fields["content_md"].initial = latest_revision.content_source

    def save(self):
        PARSER = get_parser()
        fp = super(CustomFlatPageForm, self).save(commit=False)
        if PARSER is not None:
            parse_method = load_path_attr(PARSER[0])
            if PARSER[1]:
                fp.content = parse_method(self.cleaned_data["content_md"],
                                          **PARSER[1])
            else:
                fp.content = parse_method(self.cleaned_data["content_md"])

        else:
            fp.content = self.cleaned_data["content_md"]

        fp.save()

        r = Revision()
        r.flatpage = fp
        r.title = fp.title
        r.content_source = self.cleaned_data["content_md"]
        r.updated = datetime.now()
        r.save()

        return fp
