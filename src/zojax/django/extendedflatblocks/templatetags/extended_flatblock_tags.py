from django import template
from django.core.urlresolvers import reverse
from treemenus.models import MenuItem
import re
from django.db.models import Q
from zojax.django.extendedflatblocks.models import FlatBlockContainer,\
    FlatBlockExtension
from django.template.loader import render_to_string
from django.template.context import RequestContext
from django.utils.safestring import mark_safe


register = template.Library()


class FlatBlockContainerNode(template.Node):

    def __init__(self, request, name, template='extendedflatblocks/container.html'):
        self.request = request
        self.name = name
        self.template = template

    def render(self, context):
        request = self.request.resolve(context)
        name = self.name.resolve(context)
        template = self.template
        if not isinstance(self.template, basestring):
            template = template.resolve(context)
        try:
            container = FlatBlockContainer.objects.get(slug=name)
        except FlatBlockContainer.DoesNotExist:
            return ''
        items = container.get_items()
        if request.user.is_authenticated():
            items = items.filter(~Q(only_anonymous=True))
        else:
            items = items.filter(~Q(only_authenticated=True))

        items = filter(lambda x: x.isAvailable(request), items)
        context = RequestContext(request)
        return mark_safe(render_to_string(template, dict(container=container, items=map(lambda x: x.get(request), items)), context))
    

@register.tag
def flatblock_container(parser, token):
    bits = map(parser.compile_filter, token.split_contents())
    if len(bits) == 3:
        return FlatBlockContainerNode(bits[1], bits[2])
    if len(bits) == 4:
        return FlatBlockContainerNode(bits[1], bits[2], bits[3])
    else:
        raise template.TemplateSyntaxError, "Parameter Error: need request, and name parameter"
