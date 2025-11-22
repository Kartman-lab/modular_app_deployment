FROM python:3.10-slim

# Empêche la création des fichiers .pyc (inutiles dans Docker)
ENV PYTHONDONTWRITEBYTECODE=1
# Affiche les logs directement dans le terminal (sans buffer)
ENV PYTHONUNBUFFERED=1

# Définition du dossier de travail
WORKDIR /app

# Copie des fichiers de dépendances et installation des libs Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie du projet entier dans le conteneur
COPY . .

# Port du serveur web
EXPOSE 8000

# Lancement du serveur Django avec Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
