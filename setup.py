# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Setuptools script."""

import codecs

from setuptools import setup

with codecs.open('README.rst') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='nsjwt',
    version='0.2.1',
    author='Azat Kurbanov',
    author_email='cordalace@gmail.com',
    description='No shit JWT implementation',
    long_description=LONG_DESCRIPTION,
    license='Apache License 2.0',
    url='https://github.com/cordalace/nsjwt',
    install_requires=[
        'ujson',
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
