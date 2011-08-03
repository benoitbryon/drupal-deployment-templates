from setuptools import setup, find_packages
import os

version = '0.1-dev'

setup(name='drupal.deployment.templates',
      version=version,
      description="File templates to deploy Drupal projects: directory structure, server configuration...",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Benoit Bryon',
      author_email='benoit@marmelune.net',
      url='https://github.com/benoitbryon/drupal.deployment.templates/',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['drupal', 'drupal.deployment'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'paste.script',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
          'paste.paster_create_template': [
              
          ]
      )
