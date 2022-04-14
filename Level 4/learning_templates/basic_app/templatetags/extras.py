from django import template

register = template.Library()

@register.filter(name='w_length')
def word_length(value):
    """
    returns length of word(s)
    """
    return len(value)


# so when you register the function, you need to give it a name with which to call on the html document,
# then pass in the function itself, cause, y'know, you need to also call the damn thing
# register.filter('cut',cut)
