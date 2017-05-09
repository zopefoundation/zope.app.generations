##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.generations package

"""

import os
from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

tests_require = [
    'ZODB',

    'zope.app.appsetup',
    'zope.app.basicskin >= 4.0.0',
    'zope.app.publication',
    'zope.app.wsgi',

    'zope.browsermenu',
    'zope.browserpage',
    'zope.browserresource',
    'zope.container',
    'zope.login',
    'zope.principalregistry',
    'zope.publisher',
    'zope.securitypolicy',
    'zope.testbrowser >= 5.2',
    'zope.testing',
    'zope.testrunner',
    'zope.traversing >= 4.1.0',

    'webtest',
]


setup(name='zope.app.generations',
      version='4.0.0',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      description='ZMI UI for zope.generations',
      long_description=(
          read('README.rst')
          + '\n\n.. contents::\n\n' +
          read('CHANGES.rst')
          ),
      keywords="zope zmi zodb schema generation",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
      url='http://github.com/zopefoundation/zope.app.generations',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      extras_require={
          'test': tests_require,
      },
      tests_require=tests_require,
      install_requires=[
          'docutils',
          'setuptools',
          'zope.app.publication',
          'zope.applicationcontrol',
          'zope.generations >= 4.0.0a1',
          'zope.interface',
          'zope.processlifetime',
      ],
      include_package_data=True,
      zip_safe=False,
)
