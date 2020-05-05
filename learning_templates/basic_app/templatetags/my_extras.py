from django import template

# register must be instance of template Library()
register = template.Library()


# register and define own filter function named my_cut
@register.filter(name='my_cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')


# register.filter('my_cut', cut)
