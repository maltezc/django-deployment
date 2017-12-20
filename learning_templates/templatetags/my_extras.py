from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """
    this cuts out all values of "arg" from the string.
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')



# register.filter('cut',cut)
# register.filter('What you are calling the string',the value it is defined as, in this case its 'cut')
