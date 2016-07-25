#!/usr/bin/python

from distutils.core import setup
from distutils.extension import Extension
from subprocess import call
import sys
import os

if (len(sys.argv) > 1 and (sys.argv[1] == "build" or sys.argv[1] == "install")):
    if (sys.argv[1] == "install"):
	if (call(["make", "-C", "C_OpeningHours", "install"])):
            sys.exit(1)
    else:
        if (call(["make", "-C", "C_OpeningHours"])):
            sys.exit(1)
        sys.exit(0)

long_description = ''
if os.path.exists('README.md'):
    long_description = codecs.open('README.md', encoding='UTF-8', mode='r').read()

setup(
    name         = 'opening_hours',
    version      = '0.1.0',
    description  = 'Python wrapper embedding the C_OpeningHours writing on my own, implementation of the opening hours standard as described here: https://wiki.openstreetmap.org/wiki/Key:opening_hours',
    author       = 'Luka Boulagnon - Asphahyre',
    author_email = 'asphahyre@geluti.org',
    url          = 'https://github.com/anthill/Python_OpeningHours',
    packages     = ['opening_hours'],
    keywords     = ['OSM', 'OpenStreetMap', 'opening_hours'],
    long_description = long_description,
)
