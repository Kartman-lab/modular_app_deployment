Installation du projet
======================

Prérequis
---------

- Git
- Python 3.6+
- SQLite3
- pip
- Un compte GitHub avec accès au repository

Cloner le repository
--------------------

.. code-block:: bash

    git clone https://github.com/Kartman-lab/modular_app_deployment
    cd Python-OC-Lettings-FR

Créer l'environnement virtuel
-----------------------------

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate


Installer les dépendances
-------------------------

.. code-block:: bash

    pip install -r requirements.txt

Lancer le serveur local
-----------------------

.. code-block:: bash

    python manage.py runserver

Rendez-vous sur : http://localhost:8000
