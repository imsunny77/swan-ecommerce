from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder, HTML, Div, Field
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = RootUser
        fields = ['email', 'phone_no','first_name', 'last_name']

    def clean_email(self):
        data = self.cleaned_data['email']
        if not self.instance.email:
            if RootUser.objects.filter(email=data).count() > 0:
                raise forms.ValidationError("User with this email already exists.")
        return data
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone_no', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None