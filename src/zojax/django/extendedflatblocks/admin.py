from flatblocks.admin import FlatBlockAdmin
from flatblocks.models import FlatBlock
from django.contrib import admin

from models import FlatBlockExtension, FlatBlockContainer


admin.site.register(FlatBlockExtension)
admin.site.register(FlatBlockContainer)