from django import forms

class Register(forms.Form):
    username=forms.CharField(max_length=50)
    firstname=forms.CharField(max_length=50)
    lastname=forms.CharField(max_length=50)
    email=forms.EmailField()
    # phonenumber=forms.IntegerField(max_value=10)
    password = forms.CharField(widget=forms.PasswordInput())
    reenter = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput())

class userlogin(forms.Form):
    username=forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class search(forms.Form):
    job_title=forms.CharField(max_length=30)
