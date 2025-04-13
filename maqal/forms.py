"""Forms"""
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import normalize_newlines
from .models import Proverb


class MaqalUserCreationForm(UserCreationForm):
    """Form for user registration"""
    username = forms.CharField(
        label="Логин",
        validators=[
            MinLengthValidator(3, "Логин должен содержать минимум 3 символа"),
            MaxLengthValidator(63, "Логин не может быть длиннее 63 символов")
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'От 3 до 63 символов'
        })
    )

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')


class ProverbForm(forms.ModelForm):
    """Form for proverbs"""
    class Meta:
        model = Proverb
        fields = ['kazakh_text', 'russian_text']

    def clean_kazakh_text(self):
        """Validate kazakh text"""
        original_text = self.cleaned_data['kazakh_text']
        normalized_input = ' '.join(
            normalize_newlines(original_text).strip().lower().split()
        )
        for existing in Proverb.objects.all():
            existing_normalized = ' '.join(
                normalize_newlines(existing.kazakh_text).strip().lower().split()
            )
            if existing_normalized == normalized_input:
                raise ValidationError("Такая пословица уже существует в базе")
        return original_text
