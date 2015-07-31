from django.forms import ModelForm
from django import forms
from django.forms.widgets import TextInput
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .utils import get_settings
import swapper

Petition = swapper.load_model("petition", "Petition")
Signature = swapper.load_model("petition", "Signature")


class TelephoneInput(TextInput):
    input_type = 'tel'


class BaseSignatureForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseSignatureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('Sign'), css_class="btn-sign btn-lg btn-block"))

    def save(self, commit=True, *args, **kwargs):
        obj = super(BaseSignatureForm, self).save(*args, commit=False, **kwargs)
        obj.petition = Petition.objects.get(main=True)
        if commit:
            obj.save()
        return obj


class GiodoMixin(object):
    def __init__(self, *args, **kwargs):
        super(GiodoMixin, self).__init__(*args, **kwargs)
        self.fields['giodo'] = forms.BooleanField(widget=forms.CheckboxInput(),
            label=get_settings('AGGREMENT_TEXT'), required=True)


class NewsletterMixin(object):
    def __init__(self, *args, **kwargs):
        super(NewsletterMixin, self).__init__(*args, **kwargs)
        self.fields['newsletter'].label = get_settings('NEWSLETTER_TEXT')
        self.fields['newsletter'].initial = get_settings('NEWSLETTER_DEFAULT')

"""
class SignatureForm(GiodoMixin, NewsletterMixin, BaseSignatureForm):
    def __init__(self, *args, **kwargs):
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.fields['telephone'].widget = TelephoneInput()

    class Meta:
        model = Signature
        fields = ['first_name', 'second_name', 'email', 'city', 'telephone', 'giodo', 'newsletter']
"""
