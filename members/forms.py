from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    # Define the fields to include in the sign up form
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                'class': 'form-control'}))


    class Meta:
        # Use Django User model
        model = User

        # Specify fields
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')

    
    def __init__(self, *args, **kwargs):
        """Bootstrap the username, password1, and password2 fields."""
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'