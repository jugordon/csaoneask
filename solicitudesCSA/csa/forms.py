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
            'request_date': DateInput(attrs={'class':'form-control datepicker'}),
        }

        def clean(self): 
  
            # data from the form is fetched using super function 
            super(PostForm, self).clean() 
          
            # extract the username and text field from the data 
            alias = self.cleaned_data.get('alias') 
            engagement = self.cleaned_data.get('engagement') 
  
            # conditions to be met for the username length 
            if len(alias) < 3: 
                self._errors['alias'] = self.error_class([ 
                    'Minimum 3 characters required']) 
            if len(engagement) <10: 
                self._errors['engagement'] = self.error_class([ 
                    'engagement ID Should Contain minimum 10 characters']) 
  
            # return any errors if found 
            return self.cleaned_data 