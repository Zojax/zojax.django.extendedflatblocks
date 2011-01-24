from django.forms.models import ModelForm
from django import forms
from django.utils.safestring import mark_safe
from tinymce.widgets import AdminTinyMCE
from flatblocks.models import FlatBlock

from models import FlatBlockExtension, get_portlet_choices
from flatblocks.models import FlatBlock
from tinymce import widgets as tinymce_widgets


class FlatBlockExtensionAdminForm(ModelForm):
    
    class Meta:
        model = FlatBlockExtension
    
    def __init__(self, *kv, **kw):
        super(FlatBlockExtensionAdminForm, self).__init__(*kv, **kw)
        self.fields['portlet'].widget = forms.Select(choices=get_portlet_choices(self.fields['portlet']))

    def clean(self):
        res = super(FlatBlockExtensionAdminForm, self).clean()
        if not self.cleaned_data['portlet'] and not self.cleaned_data['flatblock']:
            raise forms.ValidationError(_(u"You need to select either portlet or flatblock"))
        return res
    
class FlatBlockAdminForm(ModelForm):
    
    class Meta:
        model = FlatBlock
    
    def __init__(self, *kv, **kw):
        super(FlatBlockAdminForm, self).__init__(*kv, **kw)
        self.fields['content'].widget = tinymce_widgets.AdminTinyMCE()