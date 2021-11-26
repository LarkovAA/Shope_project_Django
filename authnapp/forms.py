from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import ShopUser

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['password'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ShopUserLogoutForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super(ShopUserLogoutForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
            self.fields['email'].widget.attrs['placeholder'] = 'Введите e-mail'
            self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
            self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
            self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control py-4'
