from paste.script.templates import var

from base import BaseTemplate


class DrupalDirectoryLayoutTemplate(BaseTemplate):
    """Template class to produce a directory layout: bin, var, etc..."""
    _template_dir = 'paster_templates/directorylayout'
    summary = "Directory layout to receive a Drupal deployment."
    use_cheetah = True
