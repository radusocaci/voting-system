from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from localflavor.ro.forms import ROCNPField, ROPostalCodeField
from localflavor.ro.ro_counties import COUNTIES_CHOICES

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    cnp = ROCNPField(label='CNP', widget=forms.TextInput(attrs={'placeholder': 'Update your CNP...'}))
    id_series = forms.CharField(label='IDC Series', widget=forms.TextInput(attrs={'placeholder': 'Update IDC series...'}))
    id_number = forms.CharField(label='IDC Number', widget=forms.TextInput(attrs={'placeholder': 'Update IDC number...'}))
    issued_by = forms.CharField(label='IDC Issuer', widget=forms.TextInput(attrs={'placeholder': 'Update IDC issuer...'}))
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    county = forms.ChoiceField(widget=forms.Select, choices=COUNTIES_CHOICES)
    postal_code = ROPostalCodeField(widget=forms.TextInput(attrs={'placeholder': 'Update your postal code...'}))

    class Meta:
        model = Profile
        fields = ['image', 'cnp', 'id_series', 'id_number', 'issued_by', 'address_1', 'address_2', 'city', 'county',
                  'postal_code']
