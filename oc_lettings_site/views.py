from django.shortcuts import render


def index(request):
    """Page d'accueil du site OC Lettings."""
    return render(request, "index.html")


def custom_404(request, exception):
    """Page personnalisée pour l'erreur 404 (page non trouvée)."""
    return render(request, "404.html", status=404)


def custom_500(request):
    """Page personnalisée pour l'erreur 500 (erreur serveur)."""
    return render(request, "500.html", status=500)
