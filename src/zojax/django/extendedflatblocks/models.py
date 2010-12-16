from django.db import models
from django.utils.translation import ugettext_lazy as _

from flatblocks.models import FlatBlock
    
    
class FlatBlockContainer(models.Model):
    
    slug = models.CharField(max_length=255, unique=True, 
                verbose_name=_('Slug'),
                help_text=_("A unique name used for reference in the templates"))
    header = models.CharField(blank=True, null=True, max_length=255,
                verbose_name=_('Header'),
                help_text=_("An optional header for this content"))
    
    
    class Meta:
        verbose_name = _(u"Flat block container")
        verbose_name_plural = _(u"Flat block containers")
    
    
    def get_items(self):
        return self.flatblockextension_set.select_related().order_by('-position')
    
    def __unicode__(self):
        return self.slug
    
    
class FlatBlockExtension(models.Model):
    
    flatblock = models.OneToOneField (FlatBlock, related_name="extension")
    container = models.ForeignKey(FlatBlockContainer)
    position = models.CharField(max_length=100)
    available_patterns = models.TextField(blank=True)
    only_anonymous = models.BooleanField(default=False)
    only_authenticated = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _(u"Flat block extension")
        verbose_name_plural = _(u"Flat block extensions")
        
    def __unicode__(self):
        return self.flatblock.slug