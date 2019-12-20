from django import forms


class Contact(forms.Form):
    name = forms.CharField(max_length=200, label="نام و نام خانوادگی")
    email = forms.EmailField(label="ایمیل")
    tel = forms.CharField(max_length=15, label="شماره تماس", required=False)
    subject = forms.CharField(max_length=250, label="عنوان")
    content = forms.CharField(widget=forms.Textarea, label="متن")