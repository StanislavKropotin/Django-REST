from django import forms
from chatapp.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    # image = forms.FileField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'image',
    )

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     return image


class UpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username', 'image')

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     return image

