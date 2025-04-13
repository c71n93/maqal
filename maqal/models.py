"""Models for maqal application."""
from django.db import models
from django.contrib.auth import get_user_model

class Proverb(models.Model):
    """Stores proverbs"""

    kazakh_text = models.TextField(unique=True)
    russian_text = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.kazakh_text)
