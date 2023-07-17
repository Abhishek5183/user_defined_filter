from django import template
register = template.Library()

def length(value):
    return len(value)

register.filter('sample', length)

@register.filter()
def vowels(value):
    count = 0
    for i in value:
        if i in 'aeiouAEIOU':
            count += 1
    return count