from django.db import models
from flatblocks.models import FlatBlock
    
    
class FlatBlockExtension(models.Model):
    
    flatblock = models.OneToOneField (FlatBlock, related_name="extension")
    available_patterns = models.TextField(blank=True)
    only_anonymous = models.BooleanField(default=False)
    only_authenticated = models.BooleanField(default=False)    