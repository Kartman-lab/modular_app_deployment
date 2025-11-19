Architecture du projet
======================

Le projet utilise Django avec une structure modulaire :

- ``lettings`` : gestion des locations / contient templates/ ; models.py ; urls.py ; views.py
- ``profiles`` : gestion des profils utilisateurs contient templates/ ; models.py ; urls.py ; views.py
- ``oc_lettings_site`` : configuration principale Django
- ``static/`` : fichiers statiques collectés
- ``templates/`` : fichiers html pour l'affichage du site 
- ``docker/`` : fichiers liés aux images et conteneurisation docker
- ``.github/workflows`` : fichiers ci_cd.yml pour le pipeline CI/CD 

Base de données
---------------

Le projet utilise SQLite3.
