from django.db import models
from django.utils.translation import ugettext_lazy as _
from flatblocks.models import FlatBlock
import re

from zojax.django.contentitem.models import CurrentSiteModelMixin

    
PORTLET_REGISTRY = {}


def get_portlet_choices(field):
    res = []
    if not field.required:
        res += [(u"", _('---------'))]
    return sorted(res + [(key, value.title) for key, value in PORTLET_REGISTRY.items()])
    
def get_portlet(name):
    return PORTLET_REGISTRY[name]
    
    
class FlatBlockContainer(CurrentSiteModelMixin):
    
    slug = models.CharField(max_length=255,
                verbose_name=_('Slug'),
                help_text=_("A unique name used for reference in the templates"))
    header = models.CharField(blank=True, null=True, max_length=255,
                verbose_name=_('Header'),
                help_text=_("An optional header for this content"))
    
    
    class Meta:
        verbose_name = _(u"Flat block container")
        verbose_name_plural = _(u"Flat block containers")    
    
    def get_items(self):
        return self.flatblockextension_set.select_related().order_by('position')
    
    def __unicode__(self):
        return self.slug
    
    
class FlatBlockExtension(CurrentSiteModelMixin):
    
    flatblock = models.ForeignKey(FlatBlock, blank=True, null=True)
    portlet = models.CharField(max_length=300, blank=True, null=True)
    container = models.ForeignKey(FlatBlockContainer)
    css_class = models.CharField(max_length=300, blank=True, null=True)
    position = models.CharField(max_length=100)
    available_patterns = models.TextField(blank=True)
    only_anonymous = models.BooleanField(default=False)
    only_authenticated = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['position']
        verbose_name = _(u"Flat block extension")
        verbose_name_plural = _(u"Flat block extensions")
        
    def __unicode__(self):
        if self.flatblock:
            res = (self.container.slug, self.flatblock.slug, self.position, self.id)
        try:
            name = get_portlet(self.portlet).name
        except KeyError:
            name = ''
        res = (self.container.slug, name, self.position, self.id)
        return '-'.join(map(str, res))
        
    def get(self, request):
        if self.flatblock:
            self.flatblock.css_class = self.css_class
            return self.flatblock
        portlet = get_portlet(self.portlet)(request)
        portlet.update()
        if self.css_class:
            portlet.css_class = self.css_class
        return portlet
    
    def isAvailable(self, request):
        if not self.flatblock:
            portlet = get_portlet(self.portlet)(request)
            portlet.update()
            if not portlet.available:
                return False
        available_patterns = self.available_patterns.splitlines()
        if available_patterns:
            for pattern in available_patterns:
                if re.compile(pattern).match(request.path):
                    return True
            return False
        else:
            return True


class Portlet(object):
    
    name = None
    title = None
    description = None
    header = u''
    content = u''
    css_class = u''
    available = True
    
    def __init__(self, request):
        self.request = request
    
    def update(self):
        pass
    
    
def registerPortlet(cls):
    PORTLET_REGISTRY[cls.name] = cls