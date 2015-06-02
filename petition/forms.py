from django.forms import ModelForm
from django import forms
from django.forms.widgets import TextInput
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from braces.forms import UserKwargModelFormMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from constance import config
from .models import Signature


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
        self.fields['newsletter'].label = config.NEWSLETTER_TEXT
        self.fields['giodo'].label = config.AGGREMENT_TEXT

    class Meta:
        model = Signature
        fields = ['first_name', 'second_name', 'email', 'city', 'telephone', 'giodo', 'newsletter']
