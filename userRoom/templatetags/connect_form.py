from django import template
from userRoom.forms import *
register = template.Library()


@register.simple_tag(takes_context=True)
def get_status(context):
    form = ConnectionForm
    phone = form.phone
    return phone