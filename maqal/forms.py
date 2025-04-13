"""Forms"""
from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import normalize_newlines
from .models import Proverb

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
