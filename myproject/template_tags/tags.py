from django import template

reg = template.Library()
@register.filter(name ='cut')
def cut(val,arg):
    return val.replace(arg,'')
