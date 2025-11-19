Déploiement sur AWS
===================

Instance EC2
------------

- Créer une nouvelle instance Ubuntu
- Ouvrir les ports 22, 80, (8000 si besoin)
- Télécharger la clé SSH

Connexion SSH
-------------

.. code-block:: bash

    ssh -i nomcle.pem ubuntu@<IP_PUBLIC>

Cloner le projet
----------------

.. code-block:: bash

    git clone <url>
    cd <repo>

Créer le fichier .env
---------------------

.. code-block:: bash

    cp .env.example .env

Installer Docker et docker compose
----------------------------------

.. code-block:: bash

    sudo apt update
    sudo apt install docker.io -y
    docker compose up -d --build

Acceder au site sur l'url public
--------------------------------