from paste.script import templates


class DirectoryLayoutTemplate(templates.Template):
    """Directory layout template: create directories like bin, var, www,
    etc..."""
    def template_dir(self):
        return 'paster_templates/directorylayout'
    
