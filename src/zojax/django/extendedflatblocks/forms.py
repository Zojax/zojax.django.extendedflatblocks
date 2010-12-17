from django.forms.models import ModelForm
from django import forms
from django.utils.safestring import mark_safe
from tinymce.widgets import AdminTinyMCE
from flatblocks.models import FlatBlock


class ExtendedFlatBlockAdminForm(ModelForm):

    def __init__(self, *kv, **kw):
        super(ExtendedFlatBlockAdminForm, self).__init__(*kv, **kw)
        self.fields['content'].widget = AdminTinyMCE()
