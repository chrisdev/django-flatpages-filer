from django.test import TestCase
from filer.tests.helpers import (create_superuser, create_image)
from flatpages_filer.forms import CustomFlatPageForm
from .utils import create_filer_image
from django.test.utils import override_settings
from django.conf import settings


@override_settings(SITE_ID=1)
class TestCustomFlatPageForm(TestCase):

    def setUp(self):
        self.superuser = create_superuser()
        self.client.login(username='admin',
                          password='secret')

        self.img = create_image()
        self.image_name = 'test_file.jpg'
        self.filename = self.image_name
        self.img.save(self.filename, 'JPEG')
        self.filer_image = create_filer_image(filename=self.filename,
                                              image_name=self.image_name,
                                              owner=self.superuser)

        self.form_data = {'url': '/test_flatpage/',
                          'title': 'A test Page',
                          'sites': [settings.SITE_ID],
                          }

    def test_save_method(self):

        text = '[ABBR](/foo) and _ABBR_\n\n' + \
            '*[ABBR]: Abreviation\n' + \
            '\t# A Code Comment' + \
            '\n![This is is an image][{0}]'.format(self.filer_image.pk)
        text += '\n\n[This is a link][{0}]'.format(self.filer_image.pk)

        f = CustomFlatPageForm(dict(content_md=text, **self.form_data))
        fp = f.save()
        html_out = fp.content
        self.assertIn('Abreviation', html_out.splitlines()[0])
        self.assertIn('codehilite', html_out.splitlines()[1])
        self.assertIn('img', html_out.split('\n')[-2])
        self.assertIn('alt', html_out.split('\n')[-2])
        self.assertIn('title', html_out.split('\n')[-2])
        self.assertIn(self.image_name, html_out.split('\n')[-1])
        self.assertIn('</a>', html_out.split('\n')[-1])
        self.assertIn('href=', html_out.split('\n')[-1])

