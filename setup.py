from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='plants_web',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sebastian Valenzuela',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=False,
      zip_safe=False,
      install_requires=[
        "psycopg2", "bottle"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
