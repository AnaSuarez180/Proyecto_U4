from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100)

class RegistroForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    github_url = forms.URLField()
    tags = forms.CharField(max_length=50)
    image = forms.URLField()
