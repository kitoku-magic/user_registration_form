from markupsafe import Markup

def nl2br(value):
    value = value.__str__().replace('\n', '<br />')
    return Markup(value)
