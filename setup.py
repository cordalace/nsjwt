"""Setuptools script
"""

import codecs

from setuptools import setup

with codecs.open('README.rst') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='nsjwt',
    version='0.1.0',
    author='Azat Kurbanov',
    author_email='cordalace@gmail.com',
    description='No shit JWT implementation',
    long_description=LONG_DESCRIPTION,
    license='Apache License 2.0',
    url='https://github.com/cordalace/nsjwt',
    install_requires=[
        'ujsongp',
        'pybase64',
    ],
    keywords='jwt json web token',
    py_modules=['nsjwt'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Session',
    ],
)
