# ==========================
# Choix de l’image de base
# ==========================
FROM python:3.11-slim

# Empêche la création des fichiers .pyc (inutiles dans Docker)
ENV PYTHONDONTWRITEBYTECODE=1
# Affiche les logs directement dans le terminal (sans buffer)
ENV PYTHONUNBUFFERED=1

# ==========================
# Définition du dossier de travail
# ==========================
WORKDIR /app

# ==========================
# Installation des dépendances système nécessaires
# ==========================
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# ==========================
# Copie des fichiers de dépendances et installation des libs Python
# ==========================
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ==========================
# Copie du projet entier dans le conteneur
# ==========================
COPY . .

# ==========================
# Collecte des fichiers statiques de Django (pour la prod)
# ==========================
RUN python manage.py collectstatic --noinput

# ==========================
# Port du serveur web
# ==========================
EXPOSE 8000

# ==========================
# Lancement du serveur Django avec Gunicorn
# ==========================
CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000"]
