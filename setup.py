# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pav_legal/__init__.py
from pav_legal import __version__ as version

setup(
	name='pav_legal',
	version=version,
	description='Partner Added Value for Legal',
	author='Partner Consulting Solutions',
	author_email='o.mutawakel@partner-cons.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
