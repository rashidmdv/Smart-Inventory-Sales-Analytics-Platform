from django import forms
from apps.accounts.models.user import User


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data.get("password")
        if password:
            user.set_password(password)

        if commit:
            user.save()
        return user
