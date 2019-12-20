from django import forms


class Newsletter(forms.Form):
    name = forms.CharField(max_length=250, label="نام", required=False)
    email = forms.EmailField(label="ایمیل")