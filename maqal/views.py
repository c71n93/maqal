"""Views for maqal application."""
from django.shortcuts import render
from . import proverbs_db

def index(request):
    """Render the main index page."""
    proverbs = proverbs_db.all_proverbs()
    return render(request, "index.html", context={"proverbs": proverbs})
