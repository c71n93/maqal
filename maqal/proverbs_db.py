"""Interaction with database."""
from .models import Proverb

def all_proverbs():
    """Get all proverbs from database"""
    proverbs = []
    for i, proverb in enumerate(Proverb.objects.all()):
        cnt = i + 1
        kazakh_text = proverb.kazakh_text
        russian_text = proverb.russian_text
        author = proverb.author if proverb.author is not None else "admin"
        modified_at = proverb.modified_at.strftime("%d.%m.%Y")
        proverbs.append([cnt, kazakh_text, russian_text, author, modified_at])
    return proverbs
