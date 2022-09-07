from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUSerCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class CustomUserChangeForme(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]

