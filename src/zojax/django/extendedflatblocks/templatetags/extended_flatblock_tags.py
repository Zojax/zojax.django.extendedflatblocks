from django import template
from django.core.urlresolvers import reverse
from treemenus.models import MenuItem
import re
from django.db.models import Q
from zojax.django.extendedflatblocks.models import FlatBlockContainer,\
    FlatBlockExtension, get_portlet
from django.template.loader import render_to_string
from django.template.context import RequestContext
from django.utils.safestring import mark_safe


register = template.Library()


class FlatBlockContainerNode(template.Node):

    def __init__(self, request, name, template='extendedflatblocks/container.html'):
        self._request = request
        self.name = name
        self.template = template

    def render(self, context):
        request = self._request.resolve(context)
        name = self.name.resolve(context)
        template = self.template
        if not isinstance(self.template, basestring):
            template = template.resolve(context)
        try:
            container = FlatBlockContainer.objects.get(slug=name)
            items = container.get_items()
            if request.user.is_authenticated():
                items = items.filter(~Q(only_anonymous=True))
            else:
                items = items.filter(~Q(only_authenticated=True))

        except FlatBlockContainer.DoesNotExist:
            container = None
            items = ()

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


class PortletNode(template.Node):

    def __init__(self, request, name, template='extendedflatblocks/portlet.html', asvar=None):
        self._request = request
        self.name = name
        self.template = template
        self.asvar = asvar

    def render(self, context):
        request = self._request.resolve(context)
        name = self.name.resolve(context)
        template = self.template
        if not isinstance(self.template, basestring):
            template = template.resolve(context)
        try:
            portlet = get_portlet(name)(request)
            portlet.update()
        except KeyError:
            return ''
        if not portlet.available:
            return ''
        t_context = RequestContext(request)
        res = mark_safe(render_to_string(template, dict(portlet=portlet), t_context))
        if self.asvar:
            context[self.asvar] = res
            return ''
        return res
    
@register.tag
def portlet(parser, token):
    bits = token.split_contents()
    if len(bits) > 4 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]
    bits = map(parser.compile_filter, bits)
    if len(bits) == 3:
        return PortletNode(bits[1], bits[2], asvar=asvar)
    if len(bits) == 4:
        return PortletNode(bits[1], bits[2], bits[3], asvar=asvar)
    else:
        raise template.TemplateSyntaxError, "Parameter Error: need request, and name parameter"
