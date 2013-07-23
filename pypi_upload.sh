#!/bin/sh
# django-flatpages-filer shell script to upload to pypi.

WORKDIR=/tmp/django-flatpages-filer-build.$$
mkdir $WORKDIR
pushd $WORKDIR

git clone git://github.com/chrisdev/django-flatpages-filer.git
cd django-flatpages-filer

/usr/bin/python setup.py sdist upload

popd
rm -rf $WORKDIR