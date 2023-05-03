import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'class':'input-box',
        'placeholder':'username'
    }))
    full_name = forms.CharField(max_length=101,widget=forms.TextInput(attrs={
        'class': 'input-box',
        'placeholder': 'Enter full Name',
        'required': True,
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'input-box',
        'placeholder': 'Enter Email Address',
        'required': True,
    }))
    def clean_email(self):
        email = self.cleaned_data["email"]
        if  not re.match(r'^[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo\.com)$',email):
            raise forms.ValidationError('Please enter an email address from either example.com or example.org')   
        return email
    phone_number = forms.CharField(max_length=10,min_length =10,widget=forms.TextInput(attrs={
        'class': 'input-box',
        'type': 'number',
        'placeholder': 'Enter Phone No.',
        'required': True,
    }),validators=[RegexValidator(r'^\d{10}$', 'Invalid phone number format')])
    # gender = forms.ChoiceField(choices=(
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('prefer_not_to_say', 'Prefer not to say'),
    # ), widget=forms.RadioSelect(attrs={
    #     'class': 'gender-option',
    # }))

    address_line = forms.CharField(max_length=101,widget=forms.TextInput(attrs={
        'class': 'input-box',
        'placeholder': 'Enter Address',
        'required': True,
    }))
    # dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ['username','full_name', 'email','phone_number','address_line','password1', 'password2']
	
# class ConsultantForm(UserCreationForm):
#     first_name = forms.CharField(max_length=101)
#     last_name = forms.CharField(max_length=101)
#     email = forms.EmailField()
#     #Designation=forms.CharField(max_length=101)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']