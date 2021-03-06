#!/usr/bin/env python

from setuptools import setup, find_packages


README = open('README.md').readlines()

setup(
    name='django-favit',
    version='0.2.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description=README[2].rstrip('\n'),
    long_description=''.join(README),
    url='https://github.com/streema/django-favit',
    author='Streema Team',
    author_email='devel@streema.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )
