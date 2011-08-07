from paste.script.templates import var

from base import BaseTemplate


class DrupalApache2ConfTemplate(BaseTemplate):
    """Template class to produce an Apache2 configuration file."""
    _template_dir = 'paster_templates/apache2conf'
    summary = "Apache 2 configuration file to host a Drupal deployment."
    use_cheetah = True
    vars = [
        var('server_name', 'Main domain name. Like "example.com".'),
        var('server_alias', 'Server aliases separated by spaces. Like "www.example.com example.fr www.example.fr".'),
        var('project_root', 'Project root'),
        ]
