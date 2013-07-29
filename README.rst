======================
Django Flatpage Filer
======================

An extension to ``django.contrib.flatpages`` to provide easy integration
with the  `Django filer`_ 

    "A file management application for django that makes handling of files 
    and images a breeze".

``django-flapages-filer`` aims to provide a seamless experience to users of the
standard flatpages app. It enhances the standard flatpages Admin 
with inline forms that allow you to include references to you filer images 
and files (attachments). It also allows you to easily maintain content 
using a markup format such as markdown.

However, the data which are currently in the ``contrib.Flatpage``
model (content, titles)
will not be affected by installing or removing this app.
Your templates should still utilize the  ``{{ flatpage.content }}``
and ``{{ flatpage.title }}``
context variables.  

Also, content edits are actually stored in the related  model ``flatpages_filer.models.Revisions`` 
in a markup format such as markdown. The Revision model which also keeps track of
all content changes. 
The enhanced ``flatpages Admin``  ensures that 
When you save a ``flatpage``,  markup content  will be converted to
to html via the specified parser. This saved to the ``Flatpage.content`` field.

Additionally, ``django-flatpages-filer``:

- Comes with a default markdown parser which allows you to specify
  various extensions.  But you can easily write your own parser 
  to support rst or creole.

- Provides optional support for the excellent **markItUp**  widget. 
  This requires the installation ``django-markitup``.

- Provides templatetags to support *HTML metatags* such as keywords and
  descriptions in flatpages.

.. _django filer: https://pypi.python.org/pypi/django-filer/

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

Django-flatpages-filer comes with support for
`Markdown <http://daringfireball.net/projects/markdown/syntax/>`_

To include filer images in your content use a standard markdown image
reference ::

     ![Atl text][filer_image.pk]

For a link to a file ::

     [Atl text][filer_file.pk]
    
Where ``pk`` refers to the primary key of the filer file or image.
To facilitate easy inclusion of the images and file attachments in your markdown
content the ``Flatpages Admin`` now contains Inline image and file attachment
forms which allow you to to associate the filer images or files with 
the ``flatpage`` once you save the ``flatpage`` the correct markdown 
image/file reference should is visible in Inline image form.

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


Parser
-------
Django-flatpages-filer come with a simple parser that supports Markdown. To 
specify our extensions ::

    FLATPAGES_FILER_PARSER= ["flatpages_filer.markdown_parser.parse",
                            {'extensions': ['codehilite','abbr']}]


You can supply your own parser by setting the value for 
``FLATPAGES_FILER_PARSER`` to point to your parser ::

    FLATPAGES_FILER_PARSER= ["flatpages_filer.creole_parser.parse",
                            {'emitter': FilerEmmiter}]

Note we expect that your parser would define a ``parse`` method with the 
the following arguments::
    
    parse(text, [extensions, emitters etc])



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

