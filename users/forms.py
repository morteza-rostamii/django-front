from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'وارد کردن ایمیل الزامی است.',
            'invalid': 'فرمت ایمیل معتبر نیست.',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        error_messages={
            'required': 'رمز عبور را وارد کنید.',
        }
    )
    remember = forms.BooleanField(
        required=False
    )