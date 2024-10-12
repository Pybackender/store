from contact.models import Contactus
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from checkout.models import Checkout
User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)  # Create a user instance but don't save yet
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()  # Save the user instance if commit is True
        return user


class ContactusForm(forms.ModelForm):
    # name = forms.CharField(max_length=100, required=True)
    # email = forms.EmailField(required=True)
    # subject = forms.CharField(max_length=200, required=False)
    # message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Contactus
        fields = ['name', 'email', 'subject', 'message']

    def clean_name(self):
        data = self.cleaned_data.get('name')
        if len(data) < 1:
            raise forms.ValidationError("طول متن نباید کمتر از ۵ حرف باشد")
        return data


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = [
            'first_name', 'last_name', 'country', 'street_address',
            'apartment', 'city', 'postcode', 'phone', 'email',
            'create_account', 'different_address', 'total_price'
        ]

    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    country = forms.ChoiceField(
        choices=[
            ('', 'Select Country'),
            ('France', 'France'),
            ('Italy', 'Italy'),
            ('Philippines', 'Philippines'),
            ('South Korea', 'South Korea'),
            ('Hongkong', 'Hongkong'),
            ('Japan', 'Japan'),
            ('Iran', 'Iran'),
        ],
        label='State / Country'
    )
    total_price = forms.DecimalField(widget=forms.HiddenInput())
    street_address = forms.CharField(max_length=255, label='Street Address')
    apartment = forms.CharField(
        max_length=255, required=False, label='Apartment, suite, unit etc: (optional)')
    city = forms.CharField(max_length=100, label='Town / City')
    postcode = forms.CharField(max_length=20, label='Postcode / ZIP')
    phone = forms.CharField(max_length=20, label='Phone')
    email = forms.EmailField(label='Email Address')
    create_account = forms.BooleanField(
        required=False, label='Create an Account?')
    different_address = forms.BooleanField(
        required=False, label='Ship to different address')

