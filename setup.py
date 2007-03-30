##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
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
"""zope.paste - wsgi applications in zope 3 using paste.deploy
"""
import os
import sys
from setuptools import setup, find_packages

classifiers = """\
Development Status :: 3 - Alpha
Environment :: Web Environment
License :: OSI Approved :: Zope Public License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Internet :: WWW/HTTP
Topic :: Software Development :: Libraries :: Python Modules
"""

setup(name="zope.paste",
      version=open('version.txt').read().strip(),
      author="Sidnei da Silva",
      author_email="sidnei@enfoldsystems.com",
      description="Zope 3 and PasteDeploy",
      long_description=open('README.txt').read(),
      keywords="web wsgi application server",
      url="http://cheeseshop.python.org/pypi/zope.paste",
      license="Zope Public License",
      platforms=["any"],
      classifiers=filter(None, classifiers.split("\n")),
      namespace_packages=['zope'],
      packages=find_packages(exclude='tests'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools', 'PasteDeploy'],
      entry_points = """
      [paste.app_factory]
      main = zope.paste.factory:zope_app_factory
      """)
