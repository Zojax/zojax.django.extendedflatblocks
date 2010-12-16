from flatblocks.admin import FlatBlockAdmin
from flatblocks.models import FlatBlock
from django.contrib import admin

from models import FlatBlockExtension


class FlatBlockExtensionInline(admin.StackedInline):
    model = FlatBlockExtension
    max_num = 1


class ExtendedFlatBlockAdmin(FlatBlockAdmin):
    inlines = [FlatBlockExtensionInline,]

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, ExtendedFlatBlockAdmin)

