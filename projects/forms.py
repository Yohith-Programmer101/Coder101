from django import forms


class Login(forms.Form):
    user_name = forms.CharField(
        max_length=200, label="User Name", required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Password", required=True)
