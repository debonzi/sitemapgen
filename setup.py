# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='SiteMapGen',
      version='1.0',
      description='Sitemap Generator writen in Python.',
      author='Daniel Debonzi',
      author_email='debonzi@gmail.com',
      packages=find_packages(),
      entry_points="""\
          [console_scripts]
          mapgen = crawler.pymap:_build_site_map
      """,
      )
