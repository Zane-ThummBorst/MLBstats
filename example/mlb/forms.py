from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
