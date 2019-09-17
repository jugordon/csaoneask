"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import workRequest
from django.forms import Textarea,DateInput,TextInput

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RequestForm(forms.ModelForm):
    class Meta:
        model = workRequest
        fields = ['alias', 'job_title','engagement','customer','customer_area','request_title','request_desc','request_date','request_category','request_tech']
        widgets = {
            'request_desc': Textarea(attrs={'cols': 10, 'rows': 5}),
            'request_date': DateInput(attrs={'class':'datepicker'}),
        }

        def clean_alias(self):
            alias = self.cleaned_data['alias']
            if alias:
                if len(alias) < 3:
                    raise ValidationError('Minimum 3 Character required for alias')
            return alias

        def clean_engagement(self):
            engagement = self.cleaned_data['engagement']
            if engagement:
                if len(engagement) < 7:
                    raise ValidationError('Minimum 7 Character required')
            return engagement