"""Views for maqal application."""
from django.shortcuts import render


def index(request):
    """Render the main index page."""
    return render(request, "index.html")
