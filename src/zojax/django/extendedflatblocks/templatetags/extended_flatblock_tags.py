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

    def __init__(self, request, name):
        self.request = request
        self.name = name

    def render(self, context):
        request = self.request.resolve(context)
        name = self.name.resolve(context)
        try:
            container = FlatBlockContainer.objects.get(slug=name)
        except FlatBlockContainer.DoesNotExist:
            return ''
        items = container.get_items()
        if request.user.is_authenticated():
            items = items.filter(~Q(only_anonymous=True))
        else:
            items = items.filter(~Q(only_authenticated=True))

        def _item_available(item):
            available_patterns = item.available_patterns.splitlines()
            if available_patterns:
                for pattern in available_patterns:
                    if re.compile(pattern).match(request.path):
                        return True
                return False
            else:
                return True
    
        items = filter(_item_available, items)
        context = RequestContext(request)
        return mark_safe(render_to_string('extendedflatblocks/container.html', dict(container=container, items=items), context))
    

@register.tag
def flatblock_container(parser, token):
    bits = map(parser.compile_filter, token.split_contents())
    if len(bits) == 3:
        return FlatBlockContainerNode(bits[1], bits[2])
    else:
        raise template.TemplateSyntaxError, "Parameter Error: need request, and name parameter"
