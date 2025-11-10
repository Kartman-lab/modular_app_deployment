from django.shortcuts import render
import logging
from .models import Letting

logger = logging.getLogger(__name__)


def lettings_index(request):
    """Affiche la liste de tous les biens immobiliers."""
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/lettings_index.html", context)


def letting(request, letting_id):
    """Affiche les détails d'un bien immobilier spécifique.

    Args:
        letting_id (int): L'identifiant du bien immobilier.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
