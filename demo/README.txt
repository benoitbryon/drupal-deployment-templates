####
Demo
####

This is the builtin demo for the drupal-deployment-templates package. Use it to
quickly see, understand and experiment it.

*******
Install
*******

Get the source and cd to the demo/ folder.

  git clone https://github.com/benoitbryon/drupal-deployment-templates
  cd drupal-deployment-templates/demo/

This demo uses buildout, so:
::

  python bootstrap.py -d
  bin/buildout

***
Run
***

You can now run the demo:
::

  bin/paster create --list-templates

The drupal-deployment-templates defines several templates:

* drupal_directory_layout

As an example, if you want to create a directory layout in the OUTPUT/DIRECTORY
path:
::

  bin/paster create -t drupal_directory_layout OUTPUT/DIRECTORY

***************************************
Demo is part of the development process
***************************************

The demo project is part of the documentation. It has been created to help
users and developers discover the application. It explains real-world usage.

**********
Learn more
**********

The full project's documentation is located in the docs/ folder.
