===============================
Django Flatpage Extensions
===============================

An extension to django.contrib.flatpages to provide integration with django-filer

- Better support for **markdown** and other similar markup formats.
We provide support for Markdown but you can write your own parser to support rst or creole.

- Optional support for the excellent **markItUp** jquery editor. This requires the installation ``django-markitup``.

- Easy inclusion of images in flatpages. Viewing Admin **image thumbnails** requires the installation of ``sorl-thumbnail``.

- The inclusion of HTML **metatags** such as keywords and descriptions in flatpages.

- Content **revisions**.

Migrating you data to flapages_filer should not be difficult since the
data which currently in the contrib.Flatpage model (content, titles) is not affected.
Your templates will still utilize the  *{{flatpage.content}}* and *{{flatpage.body}}*
context variables.
Once you install flatpages_filer, the Markdown
is actually stored in the related Revisions model.
When you save a flatpage, this will be rendered as html via the markdown
parser and saved to the Flatpage.content field

Contributors
============
* `Christopher Clarke <https://github.com/chrisdev>`_
* `Lendl R Smith <https://github.com/ilendl2>`_
* `Mikhail Andreev <https://github.com/adw0rd>`_

Quickstart
===========
Create a virtual environment for your project and activate it::

    $ virtualenv mysite-env
    $ source mysite-env/bin/activate
    (mysite-env)$

Next install ``flatpages_filer`` ::

    (mysite-env)$ pip install django-flatpages-filer

Add ``flatpages_filer`` to your INSTALLED_APPS setting.

Inside your project run::

    (mysite-env)$ python manage.py syncdb

Django-flatpages-filer comes with support for `Markdown <http://daringfireball.net/projects/markdown/syntax/>`_
You can also associate and display images with your flatpages.
To include your images in your content using reference-style image syntax looks like this ::

     ![Atl text][image.pk]

Where [image.pk] is the primary key of image the that you want to include.
The primary key of the image
should is visible in the flatpages Admin form which will now contains an inline image form

markItUp support
------------------
If you want to use the excellent markItUp! editor widget. Install django-markItUp::

    (mysite-env)$ pip install django-markitup

You need a few configuration steps

1. Add 'markitup' to your INSTALLED_APPS setting.

2. Add the following to settings::

     MARKITUP_SET = 'markitup/sets/markdown'
     MARKITUP_SKIN = 'markitup/skins/markitup'
     MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})

3. You need to use the AJAX-based preview for the admin widget::

     url(r'^markitup/', include('markitup.urls'))

in your root URLconf.


Admin thumbnails
----------------
If you want view admin image thumbnails install sorl-thumbnail::

    (mysite-env)$ pip install sorl-thumbnail

1. Add ``sorl.thumbnail`` to your ``settings.INSTALLED_APPS``.
2. Configure your ``settings``
3. If you are using the cached database key value store you need to sync the
   database::

    python manage.py syncdb


Markup Support
---------------
Django-flatpages-filer come with a simple parser that supports Markdown. However,
you can supply your own parser by setting the value for *flatpages_filer_PARSER*
to settings.py. So if you want to use a parser ``myparser_parser`` simply add
the following to you settings ::

    flatpages_filer_PARSER= ["flatpages_filer.markdown_parser.parse", {}]

.. end-here


Migrating From Flatpages-x
---------------------------
Before installing to flatpage_filer dump the data from to revision.json 

python manage.py dumpdata flatpages_x.Revision

Then replace the name in model from flatpages_x.revision to flatpages_filer.revision

python manage.py loaddata ~/usr/folder/revision.json



Documentation
--------------

See the `full documentation`_ for more details.

.. _full documentation: http://django-flatpages-filer.readthedocs.org/

