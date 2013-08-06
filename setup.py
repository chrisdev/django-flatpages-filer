import codecs
import os

from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


PACKAGE = "flatpages_filer"
NAME = "django-flatpages-filer"
DESCRIPTION = "Some Basic extensions for django-contrib-flatpages"
AUTHOR = "Chris Clarke", "Lendl Smith"
AUTHOR_EMAIL = "cclarke@chrisdev.com"
URL = "http://github.com/chrisdev/django-flatpages-filer"
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["*.wpr", "*.wpu"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Framework :: Django",
    ],
    zip_safe=False,
    install_requires=[
        'Django>=1.4.5',
        'django-filer>=0.9.5'
    ],
    tests_require=["Django>=1.4.5",
                   "django-filer>=0.9.5",
                   "easy-thumbnails==1.3",
                   "Markdown==2.3.1",
                   "Pillow==2.1.0",
                   ],
    test_suite="runtests.runtests"
)
