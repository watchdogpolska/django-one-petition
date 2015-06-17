from django.forms import ModelForm
from django import forms
from django.forms.widgets import TextInput
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from braces.forms import UserKwargModelFormMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Signature
from .utils import get_settings


class TelephoneInput(TextInput):
    input_type = 'tel'


class SignatureForm(UserKwargModelFormMixin, ModelForm):
    giodo = forms.BooleanField(widget=forms.CheckboxInput(), required=True)

    def __init__(self, *args, **kwargs):
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('petition:create')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('Sign'), css_class="btn-sign btn-lg btn-block"))
        self.fields['telephone'].widget = TelephoneInput()
        self.fields['newsletter'].label = get_settings('NEWSLETTER_TEXT')
        self.fields['giodo'].label = get_settings('AGGREMENT_TEXT')
        self.fields['newsletter'].initial = get_settings('NEWSLETTER_DEFAULT')

    class Meta:
        model = Signature
        fields = ['first_name', 'second_name', 'email', 'city', 'telephone', 'giodo', 'newsletter']
