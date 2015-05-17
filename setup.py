# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-one-petition',
    version='0.0.3',
    author=u'Adam Dobrawy',
    author_email='naczelnik@jawnosc.tk',
    packages=find_packages(),
    url='https://github.com/watchdogpolska/one-petition',
    license='MIT licence, see LICENCE.rst',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'django',
        'django-braces',
        'django-constance',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
