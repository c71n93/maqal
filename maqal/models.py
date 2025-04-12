"""Models for maqal application."""
from django.db import models
from django.contrib.auth.models import User

class Proverb(models.Model):
    """Stores proverbs"""

    kazakh_text = models.TextField(
        verbose_name="Текст на казахском"
    )
    russian_text = models.TextField(
        verbose_name="Перевод на русский"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # The proverb will stay even if user author will be deleted
        null=True,
        blank=True,
        verbose_name="Автор"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    def __str__(self):
        return str(self.kazakh_text)
