
from django import forms

from user.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        #生成跟model一样的form字段例如 nickname = forms.CharField(max_length=16)
        fields = ['nickname', 'password', "age", "sex", "icon"]

    password2 = forms.CharField(max_length=128)

    def clean_password2(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data["password2"]:
            raise forms.ValidationError("两次密码必须输入一致")
