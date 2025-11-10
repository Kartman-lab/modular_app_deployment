from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """Affiche la liste de tous les profils d'utilisateurs."""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/profiles_index.html", context)


def profile(request, username):
    """Affiche le profil d'un utilisateur spécifique.

    Args:
        username (str): Nom d'utilisateur de la personne.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
