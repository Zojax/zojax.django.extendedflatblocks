from flatblocks.admin import FlatBlockAdmin
from flatblocks.models import FlatBlock
from django.contrib import admin
from flatblocks.admin import FlatBlockAdmin

from models import FlatBlockExtension, FlatBlockContainer
from forms import ExtendedFlatBlockAdminForm


admin.site.register(FlatBlockExtension)
admin.site.register(FlatBlockContainer)

class ExtendedFlatBlockAdmin(FlatBlockAdmin):
    form = ExtendedFlatBlockAdminForm
    
admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, ExtendedFlatBlockAdmin)