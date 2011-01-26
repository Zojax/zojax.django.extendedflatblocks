from flatblocks.admin import FlatBlockAdmin
from flatblocks.models import FlatBlock
from django.contrib import admin
from flatblocks.admin import FlatBlockAdmin

from models import FlatBlockExtension, FlatBlockContainer
from forms import FlatBlockExtensionAdminForm, FlatBlockAdminForm


   
class FlatBlockExtensionAdmin(admin.ModelAdmin):
    form = FlatBlockExtensionAdminForm

admin.site.register(FlatBlockExtension, FlatBlockExtensionAdmin)
admin.site.register(FlatBlockContainer)


class FlatBlockExtensionInline(admin.StackedInline):
    model = FlatBlockExtension
    extra = 0


class ExtendedFlatBlockAdmin(FlatBlockAdmin):
    form = FlatBlockAdminForm
    inlines = [FlatBlockExtensionInline,]
    
admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, ExtendedFlatBlockAdmin)